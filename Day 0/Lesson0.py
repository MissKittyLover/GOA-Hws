print("Day 0 Homework...")

from turtle import *

print ("♡ Mariam Ghlonti ♡")
print("")
#We want to draw a mini house...
print("")
#Step один: Draw a square (for the walls)
print("")

speed(15)
width(3)
begin_fill()
color("#bf8794")
forward(210)
left(90)

forward(160)
left(90)

forward(210)
left(90)

forward(160)
left(90)
end_fill()

#Drawing a door with golden hue and two doors ✧₊⁺
forward(80)
left(90)

color("#887949")
begin_fill()
forward(60)
right(90)

forward(50)
right(90)

forward(60)
right(90)
end_fill()

color("#bf8794")
forward(25)

color("#887949")
right(90)
forward(60)

right(90)
forward(25)

right(90)
forward(60)

color("#bf8794")
left(90)
forward(80)

left(90)
forward(160)

#Drawing a cute rooftop ❀
begin_fill()
color("#797373")
left(57)
forward(124)

left(65)
forward(127)
end_fill()

penup()
goto(80, 0)
pendown()

#Outlining our adorable house...

color("#4C442A")
right(123)
forward(60)

right(90)
forward(25)

right(90)
forward(60)

penup()
goto(105, 60)
pendown()

left(90)
forward(25)

right(90)
forward(60)

right(90)
forward(50)

color("#875e67")
forward(80)
right(90)

forward(160)
right(180)

penup()
goto(210,160)
pendown()

forward(160)
right(90)
forward(80)

penup()
goto(210, 160)
right(90)
pendown()

color("#494545")
left(57)
forward(124)

left(65)
forward(127)

penup()
goto(0, 160)
left(149)
pendown()

forward(210)

#Forgot to add winsome windows ✧₊⁺

penup()
goto(25, 20)
pendown()

#Let's make them blueish...
color("#9ABFDB")

begin_fill()
forward(30)
left(90)
forward(65)
left(90)
forward(30)
left(90)
forward(65)
end_fill()

penup()
goto(155, 20)
left(90)
pendown()

begin_fill()
forward(30)
left(90)
forward(65)
left(90)
forward(30)
left(90)
forward(65)
end_fill()

#Outlining the windows...
color("#70a3c1")
left(90)

forward(30)
left(90)
forward(65)
left(90)
forward(30)
left(90)
forward(65)

penup()
goto(25, 20)
left(90)
pendown()

forward(30)
left(90)
forward(65)
left(90)
forward(30)
left(90)
forward(65)

left(90)

#Why not add a circular window too?

color("#A7DCDF")
penup()
goto(105, 90)
pendown()

begin_fill()
circle(25)
end_fill()

color("#618a95")
circle(25)
left(90)
forward(50)

penup()
goto(80,115)
pendown()

right(90)
forward(50)

#Door knobs in ⋆˙⟡gold⋆˙⟡? 

penup()
goto(100, 26)
pendown()

color("#D1A000")
circle(1)

penup()
goto(110, 26)
pendown()

color("#D1A000")
circle(1)

penup()
goto(0, 0)
pendown()

#Finished...?

exitonclick()