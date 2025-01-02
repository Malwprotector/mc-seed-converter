#This work is licensed under a CC BY-NC-SA 4.0 License. 
#Read it here: https://creativecommons.org/licenses/by-nc-sa/4.0/

print("--------------------------------------------------")
print("-------------Minecraft seed converter-------------")
print("--------------------------------------------------")
print()
print()
print('Please note that: \n -All Bedrock seeds can be converted to Java seeds. \n -There will be some differences in the world that are generated. \n -Spawn points will likely be different. \n -Structures such as the Desert temples, Jungle Temples, Mineshafts, Strongholds will not be in the same place. \n -The Biomes and the map will be a close match to the original world seed. \n -You won’t be able to convert all Java seeds to Bedrock seeds.')
print()
print('This work is licensed under a CC BY-NC-SA 4.0 License. Read it here: https://creativecommons.org/licenses/by-nc-sa/4.0/')
print()
print()
asked_seed = input("please enter the seed: ")
minecraft_version = input("Please enter the seed version (java or bedrock): ")
new_seed = 0
seed = int(asked_seed)
print()
print("--------------------------------------------------")
print()
if minecraft_version == 'java':
    if seed <= 0:
        print('error: seed cannot be converted')
        print()
        print()
    elif seed <= 2147483648:
    	print("the seed has been successfully converted to the bedrock version. \n %s" % (seed))
    	print()
    	print()

    elif seed >= 2147483649 and seed <= 4294967296:
	    new_seed = seed - 4294967296
	    print("the seed has been successfully converted to the bedrock version. \n %s" % (new_seed))
	    print()
	    print()
    else:
	    print('error: seed cannot be converted')
	    print()
	    print()
elif minecraft_version == 'bedrock':
	if seed > 0 and seed <= 2147483648:
		print("the seed has been successfully converted to the java version. \n %s" % (seed))
		print()
		print()
	elif seed < 0:
		new_seed = seed + 4294967296
		print("the seed has been successfully converted to the java version. \n -%s" % (new_seed))
		print()
		print()
	else:
	    print('error: seed is incorrect')
else:
	print('error: invalid minecraft version')

    
