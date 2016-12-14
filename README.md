## Recitation 13

### Movies!

Run the python, then execute this command:

```
ffmpeg -framerate 10 -pattern_type glob -i "plot_*.png" -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
```

You need the program `ffmpeg` available at: (https://ffmpeg.org/)[https://ffmpeg.org/] and on package managers.
