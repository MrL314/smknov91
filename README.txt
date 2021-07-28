******************************
*  Super Mario Kart Nov'91   *
*     Prototype  Repair      *
*                            *
*         by MrL314          *
******************************
last updated: July 26, 2021


>>>>> Please read through the entire README before starting! <<<<<


If you encounter issues, see if your issue is answered in the FAQ section at the bottom.

Table of Contents:
1. Setup
2. User Manual
3. FAQ




Special Thanks:
  Sirgren
  Dirtbag
  Catador
  atomic
  SmorBjorn
  R4M0N
  SMK Workshop community
  and YOU!




DISCLAIMERS:
--------------------------------------------------------------------------
This set of scripts and programs is provided free of charge and without warranty.
It is not to be distributed with any additional files, these must be provided by 
the user at their own risk. 

This project is in no way affiliated with Nintendo. I have no connections to Nintendo,
and I have not been endorsed or sponsored by Nintendo. 









====================================================================

    Setup

====================================================================



Requirements:
 - Python 3 (https://www.python.org/downloads)
   - I recommend at least Python 3.6. See "Python Notes" below for more info.
 - bsnes-plus
   - I have provided a download mirror link below. See "BSNES Notes".
 - (Optional) bsnes-plus SFX-DOS
   - I have provided a download mirror link below. See "BSNES Notes".
     - Please use this version, as it supports the remapping needed to
       use DOS functions with Super Mario Kart




IMPORTANT NOTE:
--------------------------------------------------------------------------
To get this repair to work correctly, the .cht file, .xml file, and .srm file MUST have the 
same file name as the repaired ROM. By default this is done for you, since the repaired
ROM is named "Nov91.sfc". However, if you rename the ROM, you must also change the names
of the .xml, .cht, and .srm file to the same name. These files MUST always be in the same 
folder as the repaired ROM to work correctly.

Example: if you rename the ROM to "SMKnovember.sfc", you will also need to change the other 
files to
 - "SMKnovember.xml"
 - "SMKnovember.srm"
 - "SMKnovember.cht"







How to build:
--------------------------------------------------------------------------

Downloads and Installs:
1. Install Python. (See "Python Notes" below)
2. Download bsnes-plus. You may use the mirror link I provided above.
3. Download bsnes-plus SFX-DOS. You may use the mirror link I provided above.



Obtain files:
  !!! By obtaining these files, you do so at your own risk. !!!
1. Obtain the NEWS_05 folder from the July 24, 2020 gigaleak.
2. Obtain game.hex from NEWS_05/home/kimura/games/temp, and put in this folder.
3. Obtain drive-data from NEWS_05/home/kimura/kart/mak, and put in this folder.
4. Obtain a USA unheadered (512kb) ROM of Super Mario Kart, and put in this folder.
5. Rename the USA ROM to "Super Mario Kart (USA).sfc" if it is not already named so.
6. Obtain a dsp1b binary (usually literally called dsp1b.bin), and put in this folder.



At this point you have two options. If you are doing this just to play around with the 
Nov'91 prototype, read the instructions in "Build (Base and Fix)". However, if you are building
with the intent of research or documentation without all of my other playability fixes 
on top, read the instructions in "Build (Base Only)".






Build (Base and Fix):
1. Run "base_setup.bat". This will create the base repair, without any of the extra fixes.
  - See "Python Notes" below if you encounter issues with this step.
2. Run "extra_fixes.bat". This will enable ALL of my extra fixes for the prototype.
  - This includes SFX-DOS repairs.

Now read "SFX-DOS or not?" below to continue.





Build (Base Only):
1. Run "base_setup.bat". This will create the base repair, without any of the extra fixes.
  - See "Python Notes" below if you encounter issues with this step.

This will not apply any of the extra fixes that I have applied to the code. The only things that
are changed by the base repair are that the asset data is added, and the pointers are adjusted
accordingly so that the data will be read properly. 

Now read "SFX-DOS or not?" below to continue.






SFX-DOS or not?:

If you would like to run in bsnes-plus SFX-DOS, you may do so at this time by opening
   "Nov91.sfc" in bsnes-plus SFX-DOS. Make sure to open the cheat editor by going to 
   Tools > Cheat Editor, and enable cheats 7 and 8. Then restart the ROM.


If you instead would like to run in regular bsnes-plus, first open "Nov91.sfc" in bsnes-plus.
   Then, go to the cheat editor by going to Tools > Cheat Editor, and enable cheats 2 and 3. Then
   restart the ROM. This will disable the SFX-DOS stuff, meaning you will be able to run this on 
   regular bsnes-plus.







Python Notes:
--------------------------------------------------------------------------
- When installing Python, make sure that you select "Add to PATH" during the set up.
- Make sure that you turn off app execution aliases if using windows. Go to 
   Settings > Apps > Apps & Features > App execution aliases
   and turn off all of the ones that say "python".
- When running the setup script, if you see the message 
     "'python' is not recognized as an internal or external command, operable program
     or batch file."
  you likely will need to edit the settings in "settings.bat". Right click the file and
  click "Edit". Then edit the python_cmd variable. In most cases, it will work if you change
  the variable to one of these options:
    - "python"
    - "python3"
    - "py"
    - "py3"
  If none of those work, you will need to look up what the PATH variable was set to.






BSNES Notes:
--------------------------------------------------------------------------
This repair will ONLY work in BSNES. Due to compatibility 
issues with other emulators, this prototype cannot run in other 
emulators or on physical hardware. I apologize for the inconvenience, 
but ensuring compatibility for all emulators would cause more issues 
than it would solve.

I have made mirror links to the versions of bsnes-plus and bsnes-plus SFX-DOS that I used
while making this repair. For the most accurate results, please use these versions:
* bsnes-plus: 
        https://download1592.mediafire.com/gwscvs01pwzg/twtl3tfa902z9rc/bsnes-plus.zip
* bsnes-plus SFX-DOS: 
        https://download1338.mediafire.com/mj7pmd8d3yvg/p1qhc7pal9n0zo5/bsnes-plus-v05.79-sfx-dos.zip

For the most accurate results, I recommend using the accuracy versions. You are free to
try with other versions of bsnes, but I cannot guarantee that they will work as intended.








====================================================================

    User Manual

====================================================================

More information on controls can also be found here: https://tcrf.net/Proto:Super_Mario_Kart/November_29,_1991_Proto

This is just a compact reference just in case.



General controls:
-----------------
Start - Pause:  Works in most screens and modes. If the game seems to have frozen try pressing start to unpause
Y+B+Start+Select - Reset:  Works on all modes, use to get back to the main menu from any mode
Up/Down - Navigates the menu
Left/Right - Change menu values
B/Y - Starts with whatever menu values are selected


Main Menu:
----------
MODE
  A = Player 1/ Top screen
  B = Player 2/ Bottom screen
  MAN - Human control racer
  MON - Monitoring mode, debug values are displayed
  COM - CPU controlled racer

PLAY-1/2 - Driver selection (If MAN or COM is selected)
  PLAY-1 = Player 1 driver
  PLAY-2 = Player 2 driver
  MARIO, LUIGI, KOOPA (Bowser), PEACH (Princess), CONG (D.K. J.r.), NOKO (Koopa Troopa), KINO (Toad), YOSSY (Yoshi)

DISP-1/2 - Screen mode if MON is selected
  FR-VIEW - Same perspective as the main screen but with debug values and AI path's denoted with the tracks items
  REA-VIEW - Backwards looking view of your racer SD-VIEW - Same view as main screen, without extra sprites layers (Lakitu etc.)
  LONG-PER - View of the whole track (Similar to the final version of the game (Racers sprites are smaller than on the final version)
  NO-PERS1 - Over head view of of the whole track
  NO-PERS2 - Over head view of main racer
  NO-PERS3 - Over head view of main racer but with a keystone effect

MAP - Course selection
  CIRC = Mario Circuit
  OBAKE = Ghost Valley
  GRASS = Donut Plains
  CASTLE = Bower Castle
  ICE = Vanilla Lake
  DART = Chocolate Island SAND = Koopa Beach
  BATTLE = Battle mode test course

PROG - Mode
  RACE = Takes the MODE, PLAY-1, PLAY-2 & MAP Settings and starts a race  
  BATL = Takes the MODE, PLAY-1, PLAY-2 & MAP Settings and starts a battle
    - Note that the battle mode can be changed via ED-3)
    - Any course other than BATTLE-1 will result in a VS race style mode without checkpoints
    - Anything other than MODE MAN-MAN might result in strange effects
  ED-1 = Editor mode for setting AI Zones and Targets
  ED-2 = Editor mode for overlay items such as Item boxes and Zippers
  ED-3 = Settings


RACE Mode
---------

Just a standard race 5 laps with CPU races, once the race is over it will not progress to another track and you will need to reset back to the main menu.


BATL Mode
---------

2 Players on the track to do battle, there is no scoring but you can make the other player spin when you hit them.
If you select MAN-MAN and any normal race track (not BATTLE-1) it will result in a Vs Mode race
If you select MAN-MON it will result in a Vs Race with a CPU opponent and the MON effect selected
If you select MAN-MAN, BATTLE-1 and BATTLE (mode) 0 there will be Coins/ Balls on the track to avoid
If you select MAN-MAN, BATTLE-1 and BATTLE (mode) 1 there you can press the L Button to fire projectiles 
Use ED2 to place item boxes and save to SRAM to make it a bit more interesting. Use ED3 to Enable Machine gun mode



ED1 & 2:
--------

EDITING:
  D-PAD - Moves the cursor
  B - Places the object/value
  Y - Deletes the object/value
  SELECT - Cycles through the modes
  R-Trigger - Toggles the save menu

SAVING: 
  R-Trigger - Toggles the save options
  D-PAD - Cycles through save/ load options & Select between YES/ NO
  B - Executes the selected option
  L/S-DISK - Loads or Save to or from the Disk
  L/S-SRAM - Loads or Save to or from the SRAM
  CLEA - Remove all edited data from the course

Note if you edit a level, save to SRAM and exit to the main menu (Y+B+START+SELECT) then race/battle on that course. Then it will use your edited values.

ED1 Edit modes
  CODE  - Setting the AI Zone type
  POINT - Setting the AI Targets & Zone speeds
  SET   - Setting the AI Zone size. Each zone has specific requirements for size placement.
          Press B over the CODE tile, then move the cursor somewhere else and press B to set the size.

  See this page for the different constraints for setting the different zones:
  https://tcrf.net/Proto:Super_Mario_Kart/Debugging_Menus#7th_option_.28EDIT1.29:_AI_Zone_and_Target_editor


ED2 Edit mode Overlay editor:
  Select     - to bring up "Select Yakumono" - item selection menu.
  Up/Down    - to change item
  Left/Right - to change item's orientation

0N (Upward facing)
0E (Right facing)
0S (Downward facing)
0W (Left facing)

NIKO - Used Item box
QUES - Item/ Question Mark Box
AROW - Zipper Arrow
KABE - Multicolored Wall


ED3:
----

Y - Reduce value
B - Increase value


BATTLE - Change to 1 and return to the main menu for machine gun mode in battle mode
BOUND POWER - Collision bounce power. It’s a signed number, so anything 80h and above you need to subtract 256 from it.
MODE7 CHAR - Tile map for the course selected under MAP on the main menu
COLOR MAP - Palette set for the course selected under MAP on the main menu
MARIO - Sprite view of the 8 racers with the palette set for the course selected - Most likley this was used to make sure the drivers sprites looked correct for each theme



Fun things to try:
------------------
You can drive over water
With the right MON mode you can visually see the AI targets as you drive around
Have a battle mode with MAN-MON
Machine gun battle mode is a thing
You can use the level editor ED-2 to set item boxes on the course, save it to SRAM and then battle/ race on that track with items



Things to be aware of:
----------------------
This is early code, so it is full of bugs, the game can crash easily.
If the game can't be reset with the button combo Y+B+START+SELECT it has hard crashed and will need to be restarted.
If things get messed from a freshly booted game, try resetting the SRM file by running reset_sram.bat










====================================================================

    FAQ

====================================================================

Q: The script says "'python' is not recognized as an internal or external command, operable program
   or batch file."
A: See "Python Notes" above.


Q: The base patch batch script keeps opening up the Windows Store.
A: See "Python Notes" above.


Q: Why is the screen blue with a weird glitched sprite on the top left?
A: You are running the SFX-DOS enabled version on normal BSNES. Make sure you disable the SFX-DOS via
   the cheat editor by enabling cheats 2 and 3, then restarting the ROM.


Q: Why can't this run on snes9x, zsnes, retroarch, etc.?
A: See "BSNES Notes" above.


Q: I loaded in my data using the L-DISK command. Why is it not showing up in the race?
A: The data that gets used comes from SRAM. So, you need to first use L-DISK to load the data,
   and then use S-RAM to save it to SRAM. Then it will show up in the race.


Q: How do I download this?
A: Here's a quick download link. https://github.com/MrL314/smknov91/archive/refs/heads/main.zip



-MrL314