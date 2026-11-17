# BANANA SPLIT · MELT CLUB 3D

덩스크림 사이트 섹션 02(RIDE)의 3D 스낵게임. 이 폴더 하나가 그대로 GitHub Pages 사이트가 된다.

## 파일
- `index.html` — 게임 전체 (three.js 0.160은 jsDelivr CDN에서 불러온다)
- `dungs-glb.js` — 덩스 3D 모델(`Dungscream_final.glb`)을 스크립트로 묶은 것 (더블클릭으로 열어도 동작)
- `board-glb.js` — 바나나 보드 모델(`bananaboard.glb`)을 텍스처 빼고 묶은 것 (보드는 툰 단색으로 칠한다)
- `Dungscream_final.glb` — 덩스 원본. 메쉬 이름 `Bottom`(+귀·꼬리) · `Middle` · `Top` · `Nose` · `Eye_L`(두 눈)로 파츠를 찾는다 (.001 꼬리표 무시, 눈이 한쪽만 있으면 거울 복사)
- `bananaboard.glb` — 보드 원본. `banana` · `axis_F/B` · `part_F/B` · `wheel_L/R_F/B`
- (`dungscream.glb` — 예전 모델. 이제 쓰지 않는다)
- 모델을 고치면 `.js` 묶음도 다시 만들어야 한다: `python3 embed.py Dungscream_final.glb DUNGS_GLB dungs-glb.js` / `python3 embed.py bananaboard.glb BOARD_GLB board-glb.js --strip`
- `cover.jpg` — 공유 썸네일 / 사이트 포스터
- `images/` — 로고 · 현수막 · 벽 · 바닥 · 스티커 PNG. 같은 이름·규격으로 덮어쓰면 교체된다 (`images/README.md` 참고)

## GitHub Pages 올리기
1. GitHub에서 새 저장소 만들기 (예: `banana-split`, Public)
2. 이 폴더의 파일과 `images/` 폴더를 통째로 저장소 루트에 업로드
3. Settings → Pages → Branch `main` / `/ (root)` → Save
4. 1~2분 뒤 주소: `https://<아이디>.github.io/banana-split/`

## 프레이머 연결
버튼 링크에 위 주소를 넣고 **Open in New Tab**을 켠다.
덩스 조합을 함께 넘기려면 쿼리를 붙인다.

```
https://<아이디>.github.io/banana-split/?b=ED5579&m=754C3A&h=F2D9BC&n=cherry&bb=yellow&shop=https://스마트스토어주소
```

| 키 | 뜻 | 값 |
|---|---|---|
| `b` `m` `h` | 아래 · 가운데 · 머리 맛 색 (# 없이) | ED5579 딸기 · 754C3A 초코 · F2D9BC 바닐라 · 8FD3BE 민트초코 · F0C747 바나나 · 4AA8D1 블루베리 · A8C06B 말차 · F2A03D 망고 |
| `n` | 코 | cherry · choco · mango · blueberry · mochi · jelly |
| `bb` | 바나나 보드 색 | yellow 노랑 · green 풋바나나 · pink 핑크 · blue 블루 · mint 민트 · choco 초코 디핑 |
| `shop` | 결과 화면 `SHOP THIS DUNGS` 링크 | https:// 로 시작하는 주소 |

눈 모양은 모델 그대로 고정이다. 쿼리가 없으면 게임 타이틀의 STACK LAB에서 직접 꾸민다. 꾸민 조합·최고 점수·스티커는 그 브라우저에 저장된다.

## 디버그 (브라우저 콘솔)
`BS.startRun()` · `BS.split()` (스플릿 모드 강제) · `BS.finishRun()` (바로 결과) · `BS.store`
