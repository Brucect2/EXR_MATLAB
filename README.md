# EXR_MATLAB
Read exr files from matlab <br />
Requirements: <br />
- install pyexr
- install scipy
- install numpy
After downloading the repo, just add it to matlab default path. <br /> 
Run:
```
[img, channels] = exrread('filename.exr')
size(img)
M x N x C, C is the channel name.
```
