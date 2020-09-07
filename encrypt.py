#Librabies Required are imported
import sys
import midi

#Functions for diffent parts of the proccess.
def ascii_msg(message):
	l=[ord(i) for i in message]
	return l

#First Layer encryption with basic key
def first_layer_encryption(ascii_list,key):
	for i in range(len(ascii_list)):
		ascii_list[i]+=key
	ascii_list.reverse()
	return

#Musical Encryption, The second layer Security
def second_layer_Encryption(song,code):
	music=midi.read_midifile(song)
	for track in music:
		for event in track:
			if isinstance(event,midi.events.ProgramChangeEvent):
				actual_change = event
				
				for ascii in code:
					track.append(midi.ProgramChangeEvent(tick=0, channel=1, data=[ascii]))
				track.append(actual_change)
				midi.write_midifile("hidden_message.mid", music)
				return


if __name__=="__main__":
	message=str(input("Enter the message: "))
	key=int(input("Enter Key: "))
	code=ascii_msg(message)
	first_layer_encryption(code,key)
	song="E:\Songs\Alan Walker - Faded.mid"
	second_layer_Encryption(song,code)
