FILES:

coinInfoMainProgram.py :: The main program
better_spoken_time.py :: A subprogram for speaking
get_current_price_XXX.py ::  Subprograms that procure current prices
text_to_speech_XXX.py ::  Subprograms that then speaks out the information
variables.py :: Where you can customize the program

Configuring the hardware:

It is always a good practice to update and then upgrade one's system:

>sudo apt-get update && sudo apt-get upgrade -y

This HOWTO will assume that you have a completed module and need no instructions on how to assemble your board. Next is to config the hardware to ensure that the LCD with buttons plate is seen by the rPi and operating as expected, and will require that we modify the kernal.  The modifications needed are both within raspi-config and manually adding lines via the terminal window.  Follow:

https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

>sudo apt-get install python-smbus -y
>sudo apt-get install i2c-tools -y

Test prior to proceeding using:

https://github.com/adafruit/Adafruit_Python_CharLCD

Python Libraries Used:

The final configuration is the installation of the python libraries that the present software will use to communicate with the LCD button plate.

>cd ~
>git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git

This will now have the python libraries that the current software will look for, and if you have installed these in your /home/pi folder, modification to the code as to the location is unnecessary.

We might as well install the text-to-speech package that will be used:  festival.  Festival was used as it resides locally on the rPi and does not require any further network resources/APIs to work. This decreases the chance that an external change at will result in a breakage.  On the downside, the voice that comes with this software is a bit robot-like.  This may or may not be what you intended or like.

If you would rather have a cleaner/clearer sounding voice, then a service such as https://translate.google.com is possible.  This service will generate a sound file of a much improced upon text-to-speech output that that can then be outputed via an audio player (such as mpg123).  A search will turn up howto.  Then it is a matter of modification of the to textToSpeech_XXX.py files to make this work.
