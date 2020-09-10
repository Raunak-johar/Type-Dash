import pygame
from pygame import mixer
import random
import time
import sys


class test:

    def __init__(self):
        self.width=500;
        self.length=800;
        self.title="Let's test your fingers";
        self.result_flag=0;

        self.running=True;
        self.insidebox=False;
        self.input='';
        self.output_string='';
        self.category='';
        self.sentence='';
        self.instruction='Press ENTER to evaluate';

        self.wpm=0;
        self.words=0;
        self.letters=0;
        self.accuracy = 0;
        self.correct=0;
        self.start_time=0;
        self.time_taken=0;

        self.color_output=(0,0,0);


        self.frame=pygame.display.set_mode([self.length,self.width]);
        self.file = open("sentences.txt").read();                       # getting the sentence
        self.sentences = self.file.split('\n');

        self.restart=pygame.image.load("startbutton.png");
        self.restart=pygame.transform.scale(self.restart,(200,300));

        pygame.display.init();
        pygame.font.init();
        pygame.mixer.init();



    def reset(self):


        self.title="LET'S TEST YOUR FINGERS";
        self.input='ENTER THE TEXT HERE';
        self.output=False;
        self.insidebox=False;
        self.output_string='';
        self.result_flag=0;
        self.time_taken=0;
        self.words=0;
        self.wpm=0;
        self.sentence = random.choice(self.sentences);



    def result(self,sentence):


        self.title="RESULT:"
        self.result_flag=1;


        if sentence!=self.input:
            self.output_string="Incorrect Sentence! Try again";
            return ;

        else :
            self.time_taken=time.time()-self.start_time;

            self.words=len(sentence.split());
            self.wpm = ((self.words)/self.time_taken)*60;

            self.output_string="Time:" + str(round(self.time_taken)) + "s    WPM:"+str(round(self.wpm));

        if self.wpm!=0:
            if self.wpm<27:
                self.category='You need to practice more';
                self.color_output=(0,0,255);
            elif self.wpm>34:
                self.category="Congratulations! You're an expert";
                self.color_output=(255,255,0);
            else:
                self.category='You can get better';
                self.color_output=(0,255,0);




    def display(self,string,y,font_size,colorcode):                                       #display any string

        font = pygame.font.SysFont('sfnsdisplaycondensedthinotf', font_size);
        text = font.render(string, True, colorcode);
        text_rect = text.get_rect(center=(self.length//2, y));
        self.frame.blit(text, text_rect);



    def draw_text_box(self):                                                        #create the box
        pygame.draw.rect(self.frame, (255, 219, 0), (50,360,700,60),width=2);




    # MAIN FUNCTION
    def run(self):

        self.reset();

        while self.running:

            pygame.display.set_caption("SPEED TEST");
            self.frame.fill((0, 0, 0));
            self.display(self.title,50,40,(255,255,255));                                   #Title of the window

            if self.result_flag==0:                                                         #if user pressed enter
                self.draw_text_box();                                                       #Draws the box
                self.display(self.sentence, 300, 32,(255,219,0));                           #Sentence of the window
                self.display(self.input, 385, 30,(255,255,255));


            if self.result_flag:                                            #if output is in last window/resukt phase
                self.frame.blit(self.restart,(305,260));
                self.display(self.output_string, 108, 38,(255,255,255));
                self.display(self.category,150,38,self.color_output);

            if self.insidebox==1 and self.result_flag==0:
                self.display(self.instruction, 200, 38, (255,0,0) );

            pygame.display.update();

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False;
                    sys.exit();

                elif event.type == pygame.MOUSEBUTTONDOWN:                              #get where the cursor is pressed

                    x,y = pygame.mouse.get_pos();
                    self.start_time=time.time();

                    if x>=50 and x<=750 and y>=360 and y<=420 and self.output==0:        #in the text box /not
                        self.input='';
                        self.insidebox=True;

                    elif  x>=305 and y>=260 and self.result_flag==1 and x<=500:         #if start button is pressed again
                        self.reset();

                elif event.type ==pygame.KEYDOWN and self.insidebox:

                    if event.key==pygame.K_RETURN:
                        self.result(self.sentence);                                     #find the result

                        if self.output_string=="Incorrect Sentence! Try again":         #music file
                            transition_sound = mixer.Sound("lose.wav");                 #music file
                            transition_sound.play();

                        else:
                            transition_sound = mixer.Sound("soundeffect.wav");          #music file
                            transition_sound.play();

                    elif event.key==pygame.K_BACKSPACE:
                        self.input=self.input[0:-1];

                    elif pygame.key == pygame.K_ESCAPE:                                 #EXIT IF EXCAPE BUTTON IS PRESSED
                        self.running = False;
                        sys.exit();

                    else:

                        self.input=self.input + event.unicode;


            pygame.display.flip();



test().run();