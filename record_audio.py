import os
import time
import platform
import subprocess

#cmd=$(pactl list short  sources| awk 'NR==1{print $2}' )

#ffmpeg -f pulse -i $cmd -threads 4 out.wav -y

def kill_process():
    subpr = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    output, error = subpr.communicate()

    #procura por processos ffmpeg
    target_process = "ffmpeg"
    for line in output.splitlines():
        # quando encontra o processo
        if target_process in str(line):
            pid = int(line.split(None, 1)[0])
            os.kill( pid, 15 )    # termina o proc



def kill_ffmpeg():
    os.system( 'killall ffmpeg' )



def record_audio( file_name ):
    so = platform.system()
    if so == 'Linux' :
    
        #source=$(pactl list short  sources| awk 'NR==1{print $2}' )
        source = " pactl list short  sources| awk 'NR==1{print $2}' > driver.txt "        
        print( source )
        os.system( source)

        file_object  = open( "driver.txt", "r" )
        driver = file_object.read().split()
        driver = driver[0]   #[:-1]     # retirar o '\n'
        file_object.close()
        print( driver )
        cmd = "ffmpeg -f pulse -i " + driver + " -sample_rate 11025 -threads 4 " + file_name + " -y "
        print( cmd )
        
        proc = subprocess.Popen( cmd, stdout=subprocess.PIPE, shell=True )
        time.sleep(1)

        return proc
