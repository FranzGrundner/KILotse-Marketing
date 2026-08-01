#!/bin/bash
set -e
FFMPEG="/c/Users/ASUS Zenbook/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.2-full_build/bin/ffmpeg.exe"
cd "/c/Claude/Franz/MyTM/loom_video"
rm -f clips/*.mp4

declare -A DURATIONS=(
  ["01_hook"]=5
  ["02_wer_ich_bin"]=10
  ["03_ueberleitung"]=5
  ["04_mytm_problem"]=10
  ["05_mytm_loesung"]=15
  ["06_mynote"]=10
  ["07_mydocs_problem"]=10
  ["08_mydocs_loesung"]=15
  ["09_uebertrag"]=15
  ["10_einstieg"]=15
  ["11_cta"]=15
)
ORDER=("01_hook" "02_wer_ich_bin" "03_ueberleitung" "04_mytm_problem" "05_mytm_loesung" "06_mynote" "07_mydocs_problem" "08_mydocs_loesung" "09_uebertrag" "10_einstieg" "11_cta")

for name in "${ORDER[@]}"; do
  dur=${DURATIONS[$name]}
  "$FFMPEG" -y -loop 1 -i "slides/${name}.png" -t "$dur" -r 30 \
    -vf "format=yuv420p,scale=1920:1080" -c:v libx264 -pix_fmt yuv420p \
    "clips/${name}.mp4"
done
echo "all clips rendered"
