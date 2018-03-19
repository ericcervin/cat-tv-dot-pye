#7       | 4    |3    | 1  |11|2 6 8| 0 9 10| 5
#5 10    | 9    | 0 8 | 6  |2 |11   |1 3 4 7
#4 7 8 10| 0 9  |5    |3 11|2 |1 6

img_list = []
frame_score = [
               12,12,12,12,0,12,0,1,2,12,3,12,
               4,12,4,12,4,12,4,12,4,5,12,5,
               12,5,12,5,12,6,12,6,12,6,12,6,
               12,6,12,7,12,7,12,7,12,7,12,8,
               12,8,9,12,9,12,9,12,9,12,9,12,
               12,10,12,10,12,10,11,12,11,12,11,12
               ]

long_frame_score = []
long_frame_score.extend(frame_score)
frame_score.reverse()
long_frame_score.extend(frame_score)


def setup():
    size(540,960)
    img_list.append(loadImage("green_l00.jpg"))
    img_list.append(loadImage("green_l01.jpg"))
    img_list.append(loadImage("green_l02.jpg"))
    img_list.append(loadImage("green_l03.jpg"))
    img_list.append(loadImage("green_l04.jpg"))
    img_list.append(loadImage("green_l05.jpg"))
    img_list.append(loadImage("green_l06.jpg"))
    img_list.append(loadImage("green_l07.jpg"))
    img_list.append(loadImage("green_l08.jpg"))
    img_list.append(loadImage("green_l09.jpg"))
    img_list.append(loadImage("green_l10.jpg"))
    img_list.append(loadImage("green_l11.jpg"))
    img_list.append(loadImage("green_l_blank.jpg"))
    frameRate(24)

def draw():
    image_num = long_frame_score[frameCount % 144]
    #print image_num
    image(img_list[image_num],0,0,540,960)
    #print frameCount 
    #if frameCount < 144:
    #     saveFrame("output-####.png")