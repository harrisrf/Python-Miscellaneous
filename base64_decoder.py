import base64 as base64
import sys

with open('/mount_point1/' + sys.argv[1]) as f:
    for line in f:
        liney = line.split("|")
        liney[56] += "==="
        liney[58] += "==="
        liney[60] += "==="
        liney[62] += "==="
        liney[64] += "==="
        liney[65] += "==="
        liney[66] += "==="
		
        if liney[55] != "" and len(liney[56]) > 50:
            g = open("/mount_point1/" +liney[55].translate(None, '/'), "w")
            g.write(liney[56].decode('base64'))
            g.close()

        if liney[57] != "" and len(liney[58]) > 50:
            g = open("/mount_point1/" +liney[57].translate(None, '/'), "w")
            g.write(liney[58].decode('base64'))
            g.close()		

        if liney[59] != "" and len(liney[60]) > 50:
            g = open("/mount_point1/" +liney[59].translate(None, '/'), "w")
            g.write(liney[60].decode('base64'))
            g.close()	

        if liney[61] != "" and len(liney[62]) > 50:
            g = open("/mount_point1/" +liney[61].translate(None, '/'), "w")
            g.write(liney[62].decode('base64'))
            g.close()

        if liney[63] != "" and len(liney[64]) > 50:
            g = open("/mount_point1/" +liney[63].translate(None, '/'), "w")
            g.write(liney[64].decode('base64'))
            g.close()
        
        if len(liney[65]) > 50:
            g = open("/mount_point1/" + liney[0].zfill(6) + " - COMMS PIC - " + liney[22].translate(None, '/') + ".jpg", "w")
            g.write(liney[65].decode('base64'))
            g.close()
		
        if len(liney[66]) > 50:		
            g = open("/mount_point1/" + liney[0].zfill(6) + " - SIGN PIC - " + liney[22].translate(None, '/')+ ".jpg", "w")
            g.write(liney[66].decode('base64'))
            g.close()			
