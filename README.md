# StringArt package

This is the repository of my little coding and crafting project. I created a code that turns any picture into a string art on circular frame with defined number of nails. Not all images are suitable for this - pictures that usually work the best are pictures that have high contrast, not so many sharp edges. Faces and animals tend to work well. Landscapes, buildings and similar things usually don't. 

The algorithm I am using is described at the bottom of this README.

The python class that I created to achieve this is in a string_art.py file and notebook tutorial.ipynb demonstrates the basic functionality. File development_notebook.ipynb is my notebook that I used for development, testing and debugging.

Here is the example of an image that I decided to turn into string art:

<img src="https://github.com/otheiner/thread_art/blob/main/assets/photo.png" width="450">

And this is how the art is made. The string starts on nail 0 (you can see the line starting on the right side of the frame) and then it continues as one continuous thread. The first 100 lines is displayed below:

<img src="https://github.com/otheiner/thread_art/blob/main/assets/string_art_236_nails_100_lines.png" width="450">

... 1500 lines ...

<img src="https://github.com/otheiner/thread_art/blob/main/assets/string_art_236_nails_1500_lines.png" width="450">

... 2000 lines ...

<img src="https://github.com/otheiner/thread_art/blob/main/assets/string_art_236_nails_3000_lines.png" width="450">

And this is the snippet of the instuctions which nails to connect for the first 100 lines. It starts at nail 0, then goes to nail 182, then 154, ... The whole sequence is in ```/assets/output_sequence_236_nails.txt```.

```
----- Lines 0 to 25 ----- 

[  0 182 154 168 156]
[84 56 78 50 80]
[58 62 59 76 52]
[85 48 80 45 82]
[54 78 58 61 57] 

 ----- Lines 25 to 50 ----- 

[ 73 135  73  45  86]
[159  87 159  87  49]
[82 42 78 51 91]
[164  94 161  90 160]
[ 91 162  89  48  84] 

 ----- Lines 50 to 75 ----- 

[160  92 162  86  53]
[ 71  57 101  59  76]
[139  75 134  74  52]
[ 89 161  92  49  77]
[142  75  44  85 160] 

 ----- Lines 75 to 100 ----- 

[ 90 163  88  45  79]
[146 168 154 170 152]
[ 80  55  73 137  77]
[ 35  73  58 104  61]
[110  62 112  64 115]
```
Here is the physical art. I used 236 nails and about 900 meters of thread.

<img src="https://github.com/otheiner/string_art/blob/main/assets/physical_art.jpeg" width="450">

I can also generate images which have hole in them (this is me with open mouth), so one can get a little bit creative. The way of doing it is decribed in the tutorial notebook.

<img src="https://github.com/otheiner/thread_art/blob/main/assets/open_mouth.png" width="450">

And another image that I generated - this time not a face.

<img src="https://github.com/otheiner/thread_art/blob/main/assets/dog.png" width="450">

## The Algorithm
If you were wondering how this is achieved (without checking my code), the algorithm is surprisingly simple. 

 1) Define number of nails on circular frame, enter the image and pick the number of lines you want to draw
 2) The image is "placed inside the circular frame" and converted to greyscale
 3) The thread starts at nail number 0
 4) From all possible lines that can be drawn between nail 0 and arbitrary nail, the line that is "the darkest" is picked. This means that I sum values of all pixels that the line overlaps and I normalise it by the number of pixels on this line in order for shorter lines have same importance as long lines. If you are generating image with hole in it, just check that the line doesn't cross forbidden area and if it does, pick another line with big overlap that doesn't cross forbidden area.
 6) Once the line is picked, I subtract a little value (this value has to be tuned experimentally) from all pixels in the original image that are overlayed by the picked line.
 7) Repeat steps 4)-6) from each of the visited nails until you draw number of lines that was specified by the user in step 1)

My algorithm works with the bitmaps of the input image and masks of lines drawn between any pair of the nails. Computing these masks takes most of the time (several minutes (MacBook Pro from 2019) for a frame with ~230 nails). Time complexity of this part of the algorithm is O(n(n-1)/2), where n is the number of nails on the frame and n(n-1)/2 is number of connecitions between any pair of nails, but it has to be done only once for the frame of given number of nails. This is a reasonable trade off because once you know how many nails your frame has, you can experiment with different pictures and you won't be changing number of nails. Once these masks are saved to a cache file, algorithm is able to compute sequence of nails for any image within a few seconds. The time complexity with precomputed masks (which can be reused once they have been computed) is ~O(n) where n is the number of lines that we want to draw. Algorithm could be probably more optimised if I used vector graphics and maybe completely different approach, but since this is the solution that seems to work really well and we probably don't need to generate the image in real time for arbitrary number of nails, I decided to keep it as it is.

