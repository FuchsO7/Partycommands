import minescript
import time
import re
import random

def getcommand(command, player):
	commands = {
		"!warp":"/party warp",
		"!allinv":"/party settings allinvite true",
		"!ptme":f"/party transfer {player}",
		"!dice":f"/pc {player} rolled a {random.randint(1,6)}",
		"!f1":"/joininstance CATACOMBS_FLOOR_ONE",
		"!f2":"/joininstance CATACOMBS_FLOOR_TWO",
		"!f3":"/joininstance CATACOMBS_FLOOR_THREE",
		"!f4":"/joininstance CATACOMBS_FLOOR_FOUR",
		"!f5":"/joininstance CATACOMBS_FLOOR_FIVE",
		"!f6":"/joininstance CATACOMBS_FLOOR_SIX",
		"!f7":"/joininstance CATACOMBS_FLOOR_SEVEN",
		"!m1":"/joininstance MASTER_CATACOMBS_FLOOR_ONE",
		"!m2":"/joininstance MASTER_CATACOMBS_FLOOR_TWO",
		"!m3":"/joininstance MASTER_CATACOMBS_FLOOR_THREE",
		"!m4":"/joininstance MASTER_CATACOMBS_FLOOR_FOUR",
		"!m5":"/joininstance MASTER_CATACOMBS_FLOOR_FIVE",
		"!m6":"/joininstance MASTER_CATACOMBS_FLOOR_SIX",
		"!m7":"/joininstance MASTER_CATACOMBS_FLOOR_SEVEN",
		"!t1":"/joininstance KUUDRA_NORMAL",
		"!t2":"/joininstance KUUDRA_HOT",
		"!t3":"/joininstance KUUDRA_BURNING",
		"!t4":"/joininstance KUUDRA_FIERY",
		"!t5":"/joininstance KUUDRA_INFERNAL",
		"!b8x2":"/play bedwars_eight_two",
		"!b4x4":"/play bedwars_four_four",
		"!b4x3":"/play bedwars_four_three",
		"!b2x4":"/play bedwars_two_four",
		"!b4v4":"/play bedwars_two_four",
		"!b8x2d":f"/play bedwars_eight_two_{getdream()}",
		"!b4x4d":f"/play bedwars_four_four_{getdream()}",
	}
	return commands.get(command)

def getdream():
	dreams = ["swap","oneblock","rush","ultimate","castles","voidless","armed","lucky"]
	SecondsForDreamRotation = 82800
	WeekInSeconds = 604800
	return dreams[int(((time.time() - SecondsForDreamRotation) % (len(dreams) * WeekInSeconds)) // WeekInSeconds)]

def CheckIfInSkyblock():
	eq2 = minescript.EventQueue()
	eq2.register_chat_listener()
	minescript.execute("/locraw")
	msg = eq2.get().message
	try:
		location = eval(msg).get("gametype")
		if location == "SKYBLOCK":
			minescript.execute("/pc Play Command not allowed while playing Skyblock")
			return True
	except:
		minescript.echo(f"Error at parsing location: {msg}")
	finally:
		eq2.unregister_all()

def party():
	CheckBedwarsCommands = False
	
	eq = minescript.EventQueue()
	eq.register_chat_listener()
	minescript.echo("Party Commands enabled!")
	
	while True:
		event = eq.get()
		if not event or event.type != minescript.EventType.CHAT:
			continue
		msg = re.sub("Â§.", "", event.message)
		if msg.startswith("Party >") and msg.__contains__("!"):
			msgs = msg.split(" ")
			for i in range(1,len(msgs),1):
				if msgs[i].__contains__("!"):
					player = msgs[i-1][:-1]
					command = getcommand(msgs[i], player)
					if command:					
						if CheckBedwarsCommands and command.startswith("/play bedwars") and not CheckIfInSkyblock():
							command = None
					if command:
						time.sleep(0.5)
						minescript.execute(command)
					break
						

if __name__ == "__main__":
	party()