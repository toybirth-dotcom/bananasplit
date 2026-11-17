"""glb -> window.<VAR>="base64" 스크립트. --strip 이면 텍스처·이미지를 빼고 바이너리를 다시 묶는다."""
import base64, json, struct, sys

def read_glb(path):
    d = open(path, 'rb').read()
    jl = struct.unpack('<I', d[12:16])[0]
    j = json.loads(d[20:20 + jl])
    off = 20 + jl
    bl = struct.unpack('<I', d[off:off + 4])[0]
    return j, d[off + 8:off + 8 + bl]

def strip(j, bin_):
    j.pop('images', None); j.pop('textures', None); j.pop('samplers', None)
    for m in j.get('materials', []):
        m.pop('normalTexture', None); m.pop('occlusionTexture', None); m.pop('emissiveTexture', None)
        pbr = m.get('pbrMetallicRoughness', {})
        pbr.pop('baseColorTexture', None); pbr.pop('metallicRoughnessTexture', None)
    used = sorted({a['bufferView'] for a in j['accessors'] if 'bufferView' in a})
    remap, out = {}, bytearray()
    views = []
    for i in used:
        v = dict(j['bufferViews'][i])
        start = v.get('byteOffset', 0)
        chunk = bin_[start:start + v['byteLength']]
        while len(out) % 4: out.append(0)
        v['byteOffset'] = len(out); out += chunk
        remap[i] = len(views); views.append(v)
    for a in j['accessors']:
        if 'bufferView' in a: a['bufferView'] = remap[a['bufferView']]
    j['bufferViews'] = views
    while len(out) % 4: out.append(0)
    j['buffers'] = [{'byteLength': len(out)}]
    return j, bytes(out)

def write_glb(j, bin_):
    js = json.dumps(j, separators=(',', ':')).encode()
    while len(js) % 4: js += b' '
    total = 12 + 8 + len(js) + 8 + len(bin_)
    return (b'glTF' + struct.pack('<II', 2, total) + struct.pack('<I', len(js)) + b'JSON' + js
            + struct.pack('<I', len(bin_)) + b'BIN\x00' + bin_)

src, var, out = sys.argv[1], sys.argv[2], sys.argv[3]
do_strip = '--strip' in sys.argv
if do_strip:
    data = write_glb(*strip(*read_glb(src)))
else:
    data = open(src, 'rb').read()
note = ' (텍스처 제외 — 게임은 툰 단색으로 칠한다)' if do_strip else ''
with open(out, 'w', encoding='utf-8') as f:
    f.write('/* %s (base64)%s — file:// 로 열어도 모델을 읽을 수 있게 스크립트로 묶었다 */\n' % (src.split('/')[-1], note))
    f.write('window.%s="%s";\n' % (var, base64.b64encode(data).decode()))
print(out, len(data))
