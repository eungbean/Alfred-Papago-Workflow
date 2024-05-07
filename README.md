# Papago Workflow for Alfred 5

<div align="center">

![overview](document/overview.gif)

**쉽고 빠른 한/영, 영/한 번역이 필요해 직접 만들었습니다! <br>**

**최신 Alfred 5를 지원합니다.<br><br>**

---

🚀   빠르고 쉽게 번역을 하고 (<kbd>pp</kbd>) 결과를 복사합니다.<br>

🛸   긴 문장 번역이 필요할 때, 웹사이트에서 결과를 볼 수도 있습니다. <br>

🌎   드디어, 다양한 언어 번역을 지원합니다!<br>


<table style="width:90; text-align:center;">
    <tr>
        <td>
        <img src="https://img.shields.io/badge/Korean-white.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjUxMkgwWiIvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Im0zNTAgMzM1IDI0LTI0IDE2IDE2LTI0IDIzem0tMzkgMzkgMjQtMjQgMTUgMTYtMjMgMjR6bTg3IDggMjMtMjQgMTYgMTYtMjQgMjR6bS00MCAzOSAyNC0yMyAxNiAxNS0yNCAyNFptMTYtNjMgMjQtMjMgMTUgMTUtMjMgMjR6bS0zOSA0MCAyMy0yNCAxNiAxNi0yNCAyM3ptNjMtMjIxLTYzLTYzIDE1LTE1IDY0IDYzem0tNjMtMTUtMjQtMjQgMTYtMTYgMjMgMjR6bTM5IDM5LTI0LTI0IDE2LTE1IDI0IDIzem04LTg3LTI0LTIzIDE2LTE2IDI0IDI0Wm0zOSA0MC0yMy0yNCAxNS0xNiAyNCAyNFpNOTEgMzU4bDYzIDYzLTE2IDE2LTYzLTYzem02MyAxNiAyMyAyNC0xNSAxNS0yNC0yM3ptLTQwLTM5IDI0IDIzLTE2IDE2LTIzLTI0em0yNC0yNCA2MyA2My0xNiAxNi02My02M3ptMTYtMjIwLTYzIDYzLTE2LTE2IDYzLTYzem0yMyAyMy02MyA2My0xNS0xNiA2My02M3ptMjQgMjQtNjMgNjMtMTYtMTYgNjMtNjN6Ii8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTMxOSAzMTkgMTkzIDE5M2E4OSA4OSAwIDEgMSAxMjYgMTI2eiIvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0zMTkgMzE5YTg5IDg5IDAgMSAxLTEyNi0xMjZ6Ii8+PGNpcmNsZSBjeD0iMjI0LjUiIGN5PSIyMjQuNSIgcj0iNDQuNSIgZmlsbD0iI2Q4MDAyNyIvPjxjaXJjbGUgY3g9IjI4Ny41IiBjeT0iMjg3LjUiIHI9IjQ0LjUiIGZpbGw9IiMwMDUyYjQiLz48L2c+PC9zdmc+">
  </td>
        <td>
<img src="https://img.shields.io/badge/English-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0yNTYgMGgyNTZ2NjRsLTMyIDMyIDMyIDMydjY0bC0zMiAzMiAzMiAzMnY2NGwtMzIgMzIgMzIgMzJ2NjRsLTI1NiAzMkwwIDQ0OHYtNjRsMzItMzItMzItMzJ2LTY0eiIvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0yMjQgNjRoMjg4djY0SDIyNFptMCAxMjhoMjg4djY0SDI1NlpNMCAzMjBoNTEydjY0SDBabTAgMTI4aDUxMnY2NEgwWiIvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMjU2djI1NkgwWiIvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0xODcgMjQzIDU3LTQxaC03MGw1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIOTNsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDEybDU3IDQxLTIyLTY3em0xNjItODEgNTctNDFoLTcwbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUg5M2w1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIMTJsNTcgNDEtMjItNjdabTE2Mi04MiA1Ny00MWgtNzBsNTcgNDEtMjItNjdabS04MSAwIDU3LTQxSDkzbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUgxMmw1NyA0MS0yMi02N1oiLz48L2c+PC9zdmc+">
<img src="https://img.shields.io/badge/Japanese-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjUxMkgweiIvPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMTExLjMiIGZpbGw9IiNkODAwMjciLz48L2c+PC9zdmc+">
<img src="https://img.shields.io/badge/Chinese-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjUxMkgweiIvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Im0xNDAuMSAxNTUuOCAyMi4xIDY4aDcxLjVsLTU3LjggNDIuMSAyMi4xIDY4LTU3LjktNDItNTcuOSA0MiAyMi4yLTY4LTU3LjktNDIuMUgxMTh6bTE2My40IDI0MC43LTE2LjktMjAuOC0yNSA5LjcgMTQuNS0yMi41LTE2LjktMjAuOSAyNS45IDYuOSAxNC42LTIyLjUgMS40IDI2LjggMjYgNi45LTI1LjEgOS42em0zMy42LTYxIDgtMjUuNi0yMS45LTE1LjUgMjYuOC0uNCA3LjktMjUuNiA4LjcgMjUuNCAyNi44LS4zLTIxLjUgMTYgOC42IDI1LjQtMjEuOS0xNS41em00NS4zLTE0Ny42TDM3MC42IDIxMmwxOS4yIDE4LjctMjYuNS0zLjgtMTEuOCAyNC00LjYtMjYuNC0yNi42LTMuOCAyMy44LTEyLjUtNC42LTI2LjUgMTkuMiAxOC43em0tNzguMi03My0yIDI2LjcgMjQuOSAxMC4xLTI2LjEgNi40LTEuOSAyNi44LTE0LjEtMjIuOC0yNi4xIDYuNCAxNy4zLTIwLjUtMTQuMi0yMi43IDI0LjkgMTAuMXoiLz48L2c+PC9zdmc+">
<img src="https://img.shields.io/badge/Vietnamese-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjUxMkgweiIvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Im0yNTYgMTMzLjYgMjcuNiA4NUgzNzNMMzAwLjcgMjcxbDI3LjYgODUtNzIuMy01Mi41LTcyLjMgNTIuNiAyNy42LTg1LTcyLjMtNTIuNmg4OS40eiIvPjwvZz48L3N2Zz4=">
<img src="https://img.shields.io/badge/Thai-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjg5bC03OS4yIDE2My43TDUxMiA0MjN2ODlIMHYtODlsODIuNy0xNjkuNkwwIDg5eiIvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDg5aDUxMnY3OGwtNDIuNiA5MS4yTDUxMiAzNDV2NzhIMHYtNzhsNDAtOTIuNUwwIDE2N3oiLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAxNjdoNTEydjE3OEgweiIvPjwvZz48L3N2Zz4="></br>
<img src="https://img.shields.io/badge/Indonesian-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDI1NiAyNDkuNi00MS4zTDUxMiAyNTZ2MjU2SDB6Ii8+PHBhdGggZmlsbD0iI2EyMDAxZCIgZD0iTTAgMGg1MTJ2MjU2SDB6Ii8+PC9nPjwvc3ZnPg==">
<img src="https://img.shields.io/badge/German-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Im0wIDM0NSAyNTYuNy0yNS41TDUxMiAzNDV2MTY3SDB6Ii8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6Ii8+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTAgMGg1MTJ2MTY3SDB6Ii8+PC9nPjwvc3ZnPg==">
<img src="https://img.shields.io/badge/Spanish-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Im0wIDEyOCAyNTYtMzIgMjU2IDMydjI1NmwtMjU2IDMyTDAgMzg0WiIvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjEyOEgwem0wIDM4NGg1MTJ2MTI4SDB6Ii8+PGcgZmlsbD0iI2VlZSI+PHBhdGggZD0iTTE0NCAzMDRoLTE2di04MGgxNnptMTI4IDBoMTZ2LTgwaC0xNnoiLz48ZWxsaXBzZSBjeD0iMjA4IiBjeT0iMjk2IiByeD0iNDgiIHJ5PSIzMiIvPjwvZz48ZyBmaWxsPSIjZDgwMDI3Ij48cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMjQiIHg9IjEyOCIgeT0iMTkyIiByeD0iOCIvPjxyZWN0IHdpZHRoPSIxNiIgaGVpZ2h0PSIyNCIgeD0iMjcyIiB5PSIxOTIiIHJ4PSI4Ii8+PHBhdGggZD0iTTIwOCAyNzJ2MjRhMjQgMjQgMCAwIDAgMjQgMjQgMjQgMjQgMCAwIDAgMjQtMjR2LTI0aC0yNHoiLz48L2c+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIxMjAiIHk9IjIwOCIgZmlsbD0iI2ZmOTgxMSIgcnk9IjgiLz48cmVjdCB3aWR0aD0iMzIiIGhlaWdodD0iMTYiIHg9IjI2NCIgeT0iMjA4IiBmaWxsPSIjZmY5ODExIiByeT0iOCIvPjxyZWN0IHdpZHRoPSIzMiIgaGVpZ2h0PSIxNiIgeD0iMTIwIiB5PSIzMDQiIGZpbGw9IiNmZjk4MTEiIHJ4PSI4Ii8+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIyNjQiIHk9IjMwNCIgZmlsbD0iI2ZmOTgxMSIgcng9IjgiLz48cGF0aCBmaWxsPSIjZmY5ODExIiBkPSJNMTYwIDI3MnYyNGMwIDggNCAxNCA5IDE5bDUtNiA1IDEwYTIxIDIxIDAgMCAwIDEwIDBsNS0xMCA1IDZjNi01IDktMTEgOS0xOXYtMjRoLTlsLTUgOC01LThoLTEwbC01IDgtNS04eiIvPjxwYXRoIGQ9Ik0xMjIgMjUyaDE3Mm0tMTcyIDI0aDI4bTExNiAwaDI4Ii8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTEyMiAyNDhhNCA0IDAgMCAwLTQgNCA0IDQgMCAwIDAgNCA0aDE3MmE0IDQgMCAwIDAgNC00IDQgNCAwIDAgMC00LTR6bTAgMjRhNCA0IDAgMCAwLTQgNCA0IDQgMCAwIDAgNCA0aDI4YTQgNCAwIDAgMCA0LTQgNCA0IDAgMCAwLTQtNHptMTQ0IDBhNCA0IDAgMCAwLTQgNCA0IDQgMCAwIDAgNCA0aDI4YTQgNCAwIDAgMCA0LTQgNCA0IDAgMCAwLTQtNHoiLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTk2IDE2OGMtNyAwLTEzIDUtMTUgMTFsLTUtMWMtOSAwLTE2IDctMTYgMTZzNyAxNiAxNiAxNmM3IDAgMTMtNCAxNS0xMWExNiAxNiAwIDAgMCAxNy00IDE2IDE2IDAgMCAwIDE3IDQgMTYgMTYgMCAxIDAgMTAtMjAgMTYgMTYgMCAwIDAtMjctNWMtMy00LTctNi0xMi02em0wIDhjNSAwIDggNCA4IDggMCA1LTMgOC04IDgtNCAwLTgtMy04LTggMC00IDQtOCA4LTh6bTI0IDBjNSAwIDggNCA4IDggMCA1LTMgOC04IDgtNCAwLTgtMy04LTggMC00IDQtOCA4LTh6bS00NCAxMCA0IDEgNCA4YzAgNC00IDctOCA3cy04LTMtOC04YzAtNCA0LTggOC04em02NCAwYzUgMCA4IDQgOCA4IDAgNS0zIDgtOCA4LTQgMC04LTMtOC03bDQtOHoiLz48cGF0aCBmaWxsPSJub25lIiBkPSJNMjIwIDI4NHYxMmMwIDcgNSAxMiAxMiAxMnMxMi01IDEyLTEydi0xMnoiLz48cGF0aCBmaWxsPSIjZmY5ODExIiBkPSJNMjAwIDE2MGgxNnYzMmgtMTZ6Ii8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTIwOCAyMjRoNDh2NDhoLTQ4eiIvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Im0yNDggMjA4LTggOGgtNjRsLTgtOGMwLTEzIDE4LTI0IDQwLTI0czQwIDExIDQwIDI0em0tODggMTZoNDh2NDhoLTQ4eiIvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIzMiIgeD0iMjIyIiB5PSIyMzIiIGZpbGw9IiNkODAwMjciIHJ4PSIxMCIgcnk9IjEwIi8+PHBhdGggZmlsbD0iI2ZmOTgxMSIgZD0iTTE2OCAyMzJ2OGg4djE2aC04djhoMzJ2LThoLTh2LTE2aDh2LTh6bTgtMTZoNjR2OGgtNjR6Ii8+PGcgZmlsbD0iI2ZmZGE0NCI+PGNpcmNsZSBjeD0iMTg2IiBjeT0iMjAyIiByPSI2Ii8+PGNpcmNsZSBjeD0iMjA4IiBjeT0iMjAyIiByPSI2Ii8+PGNpcmNsZSBjeD0iMjMwIiBjeT0iMjAyIiByPSI2Ii8+PC9nPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0xNjkgMjcydjQzYTI0IDI0IDAgMCAwIDEwIDR2LTQ3aC0xMHptMjAgMHY0N2EyNCAyNCAwIDAgMCAxMC00di00M2gtMTB6Ii8+PGcgZmlsbD0iIzMzOGFmMyI+PGNpcmNsZSBjeD0iMjA4IiBjeT0iMjcyIiByPSIxNiIvPjxyZWN0IHdpZHRoPSIzMiIgaGVpZ2h0PSIxNiIgeD0iMjY0IiB5PSIzMjAiIHJ5PSI4Ii8+PHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjE2IiB4PSIxMjAiIHk9IjMyMCIgcnk9IjgiLz48L2c+PC9nPjwvc3ZnPg==">
<img src="https://img.shields.io/badge/Italian-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xNjcgMGgxNzhsMjUuOSAyNTIuM0wzNDUgNTEySDE2N2wtMjkuOC0yNTMuNHoiLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDE2N3Y1MTJIMHoiLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6Ii8+PC9nPjwvc3ZnPg==">
<img src="https://img.shields.io/badge/French-grey.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiI+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIi8+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xNjcgMGgxNzhsMjUuOSAyNTIuM0wzNDUgNTEySDE2N2wtMjkuOC0yNTMuNHoiLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAwaDE2N3Y1MTJIMHoiLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMzQ1IDBoMTY3djUxMkgzNDV6Ii8+PC9nPjwvc3ZnPg==">
        </td>
    </tr>
</table>

**[[DOWNLOAD]](https://github.com/eungbean/Alfred-Papago-Workflow/releases)**

> [!IMPORTANT]
> __오른쪽 위의 `Star⭐` 를 눌러주시면 큰 힘이 됩니다!__

</div>

## ⚡ Quickstart

### 1. 즉시 번역 및 복사하기 <kbd>pp</kbd>
<p align="center"><img src = "document/result-copy.png" height="70%" width="70%" ></p>

```
pp {문장}
```

- 문장을 즉시 한/영, 영/한 번역합니다.
- 엔터키를 누르면 클립보드로 복사합니다.


### 2. 웹사이트로 이동해 번역하기

<p align="center"><img src = "document/result-web.png" height="70%" width="70%"></p>

- 긴 문장등의 번역이 필요할 때, 브라우저에서 번역 결과를 보여줍니다.

### 3. 지원 언어 목록

- `한국어 ↔️ 영어, 일본어, 중국어 (간체, 번체), 베트남어, 인도네시아어, 태국어, 독일어, 스페인어, 이탈리아어, 프랑스어`
- 다른 언어간 번역은 추후 지원예정입니다.

## 🚀 Setup

### 0. 필수설치

(macOS Monterey 12.3 이하) Xcode의 설치가 필요합니다. [[#5](https://github.com/eungbean/Alfred-Papago-Workflow/issues/5)]
앱스토어에서 [XCode](https://developer.apple.com/download/all/?q=Xcode)를 설치해주세요.

### 1. Papago API Key 발급받기
1. NCloud 계정을 생성하고 [로그인](https://auth.ncloud.com/login) 해주세요.
2. [Console > Papago Translation API Key page](https://console.ncloud.com/papago-translation/apis)에서 `+ Application 등록`을 클릭해주세요.
![setup-0](images/setup-0.png)


3. 아래 화면에서 `Application 이름`을 입력하고 `API 선택`에서 `Papago Text Translation`, `Papago Language Detection`을 체크해주세요.
![setup-1](images/setup-1.png)


4. 성공적으로 등록이 되면 아래와 같이 표시됩니다. `API 관리` 화면에서 `인증정보` 버튼을 클릭해주세요.
![setup-2](images/setup-2.png)


5. `인증정보` 창에서 `Client ID`,`Client Secret`을 복사합니다.

6. [Alfred Workflow 설정](https://www.alfredapp.com/help/workflows/user-configuration/)에 추가해줍니다.
![setup-3](images/setup-3.png)


7. [pp 문장] 으로 번역을 테스트해보세요.
![setup-4](images/setup-4.png)

## 🧚‍♀️ Features
- [x] 한/영, 영/한 번역 기능
- [x] 바로 복사하기 및 웹사이트에서 열기
- [x] 다양한 언어쌍 번역 기능
- [ ] 타겟 언어 설정 기능
- [ ] __더 많은 기능 제안을 기다립니다!__


## ❤ Contribution is always welcome!
질문이나 버그를 발견했나요? 특정 기능이 필요하신가요?
자유롭게 새로운 이슈나 각각의 제목과 설명과 함께 PR을 제출하세요.
문제에 대한 해결책을 이미 찾았다면 망설이지 말고 공유하세요.
새로운 제안은 언제든지 환영입니다!

- (2024-05-07) https://github.com/eungbean/Alfred-Papago-Workflow/issues/7 [@dead-1ine](https://github.com/dead-1ine) [@joel-you](https://github.com/joel-you) [@taese0_0ng](https://github.com/taese0ng) Thank you for your update request for papago api shutdown issue.
*

- (2023-11) https://github.com/eungbean/Alfred-Papago-Workflow/issues/5 [@f022yo9](https://github.com/f022yo9) [@DreamingMaru](https://github.com/DreamingMaru): Thank you for discovering and resolving SSL Credential Error.

## 🎛 Workflow

![workflow](document/workflow.png)


## Licenses

이 프로젝트는 MIT 라이센스를 준수합니다.

```
MIT License
Copyright (c) 2021 eungbean
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
