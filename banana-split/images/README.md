# images — 교체용 2D 리소스

게임에서 코드로 그리던 그림을 PNG로 뽑아 둔 폴더야.
**같은 파일 이름 · 같은 규격(px)** 으로 덮어쓰면 게임이 그 이미지를 쓴다.
파일을 지우면 그 항목만 원래처럼 코드로 그린다.

| 폴더 | 파일 | 규격 (px) | 배경 | 게임 속 위치 |
|---|---|---|---|---|
| `logo/` | `logo.png` | **1400 × 760** | 투명 | 타이틀 화면 BANANA SPLIT 로고 |
| `banner/` | `banner_1_melt-club.png` · `banner_2_wet-paint.png` · `banner_3_split-zone.png` | **512 × 220** | 불투명 | 길 위 숙여서 지나가는 현수막 (3종 랜덤) |
| `wall/` | `wall_01.png` ~ `wall_10.png` | **1024 × 448** | 불투명 | 골목 좌우 벽 그래피티 현수막 (10장이 좌우로 섞여 반복) |
| `road/` | `road_1.png` ~ `road_4.png` | **512 × 1024** | 불투명 | 바닥 도로 (위가 진행 방향, 위아래 이어지게) |
| `sticker/` | `sticker_01_banana-board.png` ~ `sticker_12_melt-crown.png` | **256 × 256** | 투명 (원형) | 결과 화면 · 스티커 도감 |

## 스티커 번호
| 번호 | 이름 | 등급 |
|---|---|---|
| 01 | BANANA BOARD 바나나 보드 | COMMON |
| 02 | DRIP SCOOP 흘러내린 스쿱 | COMMON |
| 03 | CHERRY NOSE 체리 하트 코 | COMMON |
| 04 | SPRAY STAR 스프레이 별 | COMMON |
| 05 | CHECKER FLAG 체커 깃발 | COMMON |
| 06 | WET PAINT 칠 주의 | COMMON |
| 07 | SPRAY CAN 스프레이 캔 | RARE |
| 08 | SLEEPY EYES 처진 실눈 | RARE |
| 09 | SPLIT BOAT 스플릿 보트 | RARE |
| 10 | 3 TIER TOWER 3단 타워 | RARE |
| 11 | GOLD BANANA 황금 바나나 | EPIC |
| 12 | MELT CROWN 멜트 크라운 | EPIC |

## 주의
- 파일 형식은 PNG, 이름은 소문자 그대로.
- 비율이 다르면 늘어나 보인다. 규격을 꼭 맞출 것. (2배 크기로 넣어도 비율만 같으면 동작하지만 용량이 커진다)
- 로고는 그림 둘레 여백까지 포함한 크기다. 여백을 줄이면 화면에서 로고가 커진다.
- **벽 · 현수막 · 바닥**은 GitHub Pages 같은 http 주소에서 열 때만 교체된다.
  `index.html`을 더블클릭해 열면 브라우저 보안 때문에 이 셋은 기본 그림이 나온다. (로고 · 스티커는 둘 다 교체됨)
  내 컴퓨터에서 확인하려면 폴더에서 `python3 -m http.server` 실행 후 `http://localhost:8000` 접속.
