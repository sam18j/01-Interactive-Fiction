#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "275CA666-55FC-4952-8BD7-A464A095E3C3",
  "name": "Hunted Castle",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631553882881,
  "passages": [
    {
      "name": "East of the Castle",
      "tags": "",
      "id": "1",
      "text": "This is a open village east of the Castle, with run down houses all around you.\n\n[[NORTH->North of Castle]]\n[[SOUTH->South of Castle]]\n[[WEST->Grave yard]]\n[[ENTER->House]]\n[[WEST->West of Castle]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "House",
          "original": "[[ENTER->House]]"
        },
        {
          "linkText": "WEST",
          "passageName": "West of Castle",
          "original": "[[WEST->West of Castle]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a open village east of the Castle, with run down houses all around you."
    },

    current = "East of the Castle"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "North of Castle",
      "tags": "",
      "id": "2",
      "text": "You're facing the gates of the Castle, there is no one guarding the gates.\n\n[[EAST->East of the Castle]]\n[[SOUTH->South of Castle]]\n[[WEST->Grave yard]]\n[[ENTER->Castle]]\n[[WEST->West of Castle]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Castle",
          "original": "[[ENTER->Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "West of Castle",
          "original": "[[WEST->West of Castle]]"
        }
      ],
      "hooks": [],
      "cleanText": "You're facing the gates of the Castle, there is no one guarding the gates."
    },

    current = "North of Castle"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "South of Castle",
      "tags": "",
      "id": "3",
      "text": "You're facing the South side of the castle. There is a garden full of dead plants and pumpkins.\n\n[[NORTH->North of Castle]]\n[[EAST->East of the Castle]]\n[[WEST->Grave yard]]\n[[ENTER->Garden]]\n[[WEST->West of Castle]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Garden",
          "original": "[[ENTER->Garden]]"
        },
        {
          "linkText": "WEST",
          "passageName": "West of Castle",
          "original": "[[WEST->West of Castle]]"
        }
      ],
      "hooks": [],
      "cleanText": "You're facing the South side of the castle. There is a garden full of dead plants and pumpkins."
    },

    current = "South of Castle"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "Grave yard",
      "tags": "",
      "id": "4",
      "text": "This is a grave yard. Most the graves are broken down and moss growing on it.\n\n[[EAST->East of the Castle]]\n[[SOUTH->South of Castle]]\n[[NORTH->North of Castle]]\n[[WEST->West of Castle]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "West of Castle",
          "original": "[[WEST->West of Castle]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is a grave yard. Most the graves are broken down and moss growing on it."
    },

    current = "Grave yard"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "Castle",
      "tags": "",
      "id": "5",
      "text": "You entered the Castle. Theres a eerie feeling as look around. Theres a large spiral staircase and right next to the staircase there is a hallway. You hear no noise in the Castle and you feel a cool breeze.\n\n[[UP->Staircase]]\n[[ENTER->Hallway]]\n[[EAST->East of the Castle]]\n[[NORTH->North of Castle]]\n[[SOUTH->South of Castle]]\n[[WEST->Grave yard]]",
      "links": [
        {
          "linkText": "UP",
          "passageName": "Staircase",
          "original": "[[UP->Staircase]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Hallway",
          "original": "[[ENTER->Hallway]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        }
      ],
      "hooks": [],
      "cleanText": "You entered the Castle. Theres a eerie feeling as look around. Theres a large spiral staircase and right next to the staircase there is a hallway. You hear no noise in the Castle and you feel a cool breeze."
    },

    current = "Castle"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "Garden",
      "tags": "",
      "id": "6",
      "text": "You entered the garden. You pick up a dead flower but it crumbles after you pick it up. Then you accidently step in a crashed pumpkin.\n\n[[SOUTH->South of Castle]]\n[[WEST->Grave yard]]\n[[NORTH->North of Castle]]\n[[EAST->East of the Castle]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        }
      ],
      "hooks": [],
      "cleanText": "You entered the garden. You pick up a dead flower but it crumbles after you pick it up. Then you accidently step in a crashed pumpkin."
    },

    current = "Garden"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "House",
      "tags": "",
      "id": "7",
      "text": "You entered one of the houses. You see a table with two chairs, one is tipped over. There also a bed and a small kitchen. Theres a picture frame on the counter with a crossed out picture.\n\n[[SOUTH->South of Castle]]\n[[NORTH->North of Castle]]\n[[WEST->Grave yard]]\n[[EAST->East of the Castle]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        }
      ],
      "hooks": [],
      "cleanText": "You entered one of the houses. You see a table with two chairs, one is tipped over. There also a bed and a small kitchen. Theres a picture frame on the counter with a crossed out picture."
    },

    current = "House"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "Staircase",
      "tags": "",
      "id": "8",
      "text": "You're on the second floor of the Castle. You decided to walk in one of the rooms. As you walk into the room you see blood all over the floor. But then you what looks like a women staring out the window. She turns around and screams 'HELP ME' and jumps at you. You fall down and run out the room.\n\n[[DOWN->Staircase]]\n[[ENTER->Hallway]]\n[[NORTH->North of Castle]]\n[[SOUTH->South of Castle]]\n[[EAST->East of the Castle]]\n[[WEST->Grave yard]]",
      "links": [
        {
          "linkText": "DOWN",
          "passageName": "Staircase",
          "original": "[[DOWN->Staircase]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Hallway",
          "original": "[[ENTER->Hallway]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        }
      ],
      "hooks": [],
      "cleanText": "You're on the second floor of the Castle. You decided to walk in one of the rooms. As you walk into the room you see blood all over the floor. But then you what looks like a women staring out the window. She turns around and screams 'HELP ME' and jumps at you. You fall down and run out the room."
    },

    current = "Staircase"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "Hallway",
      "tags": "",
      "id": "9",
      "text": "You're are in the Hallway. You spot a weird looking door across from you, it was decorated with lion on top and vines coming out from the side of the lion. You open the door and found skeletons piled up in the middle of the floor. There was writing repeating the same words 'The Maiden is coming for you'. And the room smelled so bad that you felt like throwing up so you exit the room.\n\n[[NORTH->North of Castle]]\n[[UP->Staircase]]\n[[SOUTH->South of Castle]]\n[[EAST->East of the Castle]]\n[[WEST->Grave yard]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of Castle",
          "original": "[[NORTH->North of Castle]]"
        },
        {
          "linkText": "UP",
          "passageName": "Staircase",
          "original": "[[UP->Staircase]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of Castle",
          "original": "[[SOUTH->South of Castle]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of the Castle",
          "original": "[[EAST->East of the Castle]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Grave yard",
          "original": "[[WEST->Grave yard]]"
        }
      ],
      "hooks": [],
      "cleanText": "You're are in the Hallway. You spot a weird looking door across from you, it was decorated with lion on top and vines coming out from the side of the lion. You open the door and found skeletons piled up in the middle of the floor. There was writing repeating the same words 'The Maiden is coming for you'. And the room smelled so bad that you felt like throwing up so you exit the room."
    },

    current = "Hallway"
    response = ""
    while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]
    {
      "name": "West of Castle",
      "tags": "",
      "id": "10",
      "text": "This is the west of the Castle. There is a path that leads out of the village.",
      "links": [],
      "hooks": [],
      "cleanText": "This is the west of the Castle. There is a path that leads out of the village."
    }
  ]
}

current = "West of Castle"
response = ""
while True:
        if response == "quit":
            break
        # Find passage (update)
        current_location = {}
        for passage in world["passages"]:
          if passage["name"] == current:
              current_location = passage 
        
        # Display passage (render the world)
        print(current_location["name"])
        print(current_location["cleanText"])
        for link in current_location["links"]:
            print(link["linkText"])
        # Ask for response (get input)
        response = input("Where do you want to go?")
        for link in current_location["links"]:
            if response == link["linkText"]:
                current = link["passageName"]

if "name" in world and "passages" in world:
    print(world["name"])
    print()
    for passage in world["passages"]:
        print(passage["name"])
        print(passage["cleanText"])
        for link in passage["links"]:
            print(link["linkText"])
        print()