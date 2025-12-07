# Partycommands

A simple script for the Minescript Minecraft Mod allowing party members to control your party on Hypixel.

## Usage

Like other popular mods for Hypixel, this script allows other players in your party to control it while you are the party leader. Any party message starting with a `!` can trigger the script to execute a command. As example, `!ptme` will transfer the party to the sender, or `!f7` will start a F7 dungeon run in Hypixel Skyblock. The syntax of party commands is similar or even the same as the one of other popular mods for Hypixel. All party commands are found in a dictionary in the script, you can simply edit it to add your own party commands. There is also a check to prevent the execution of Bedwars play commands while in Skyblock, by default this is *disabled*.

### Available party commands

- `!ptme` Transfer party to sender
- `!allinv` Enable or disable the All Invite party setting
- `!dice` Roll a dice
- `!f7` Join a catacombs dungeon run in Skyblock, here Floor 7 as example
- `!m5` Join a master catacombs dungeon run in Skyblock, here Master Floor 5 as example
- `!t4` Join a kuudra run in Skyblock, here Fiery tier as example
- `!b4x4` Join a bedwars game on Hypixel, here 4v4v4v4 as example
- `!b2x8d` Join a dream bedwars game on Hypixel, here duos as example

The dungeon and kuudra play commands use `!{type}{tier}` as syntax, the bedwars play commands `!b{number of teams}x{team size}` as syntax.

Set the `CheckBedwarsCommands` variable to `True` to enable the check of Bedwars play commands.

If you want the script to automatically run when joining the Hypixel Minecraft Server, add the line `autorun[Hypixel]=partycommands` to the config.txt file of Minescript (more information about this can be found in the Minescript documentation).

## Links

- [Minescript Official Site](https://minescript.net/)
- [Minescript Discord](https://discord.gg/NjcyvrHTze)
