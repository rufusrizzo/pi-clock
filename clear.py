#!/usr/bin/python

import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

a = 0		
while a < 1:	
  segment.clear()

  a = a + 1	
  segment.write_display()
