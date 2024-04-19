from django.shortcuts import render
import subprocess
import os

def moshi(request):
    if request.method == 'POST':
        command1 = request.POST.get('command1', '')
        command2 = request.POST.get('command2', '')

        if command1:
            if any(c.isalpha() for c in command1):
                return render(request, 'baakaa.html', {'output1': f'"{command1}" Not allowed in the command'})
            elif any(c in ['. ' , ' ' , '<.' , '<~', '???-','{','}'] for c in command1):
                return render(request, 'baakaa.html', {'output1': f'"{command1}" Hehe not allowed'})
            elif command1.isdecimal():
                output1 = int(command1)*2
            else:
                try:
                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    # Set the working directory to the 'pro-player' folder
                    working_directory = os.path.join(current_directory, '..', 'pro-player')
                    output1 = subprocess.Popen(
                    ["/bin/bash", "-c", command1], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,cwd=working_directory)
                    output1 = output1.stdout.read().decode('utf-8')
                except Exception:
                    return render(request, 'baakaa.html', {'output1': f'Error executing command1: {command1}'})

        if command2:
            if any(c.isalpha() for c in command2) or " " in command2:
                return render(request, 'baakaa.html', {'output2': f'"{command2}" Not allowed in the command'})
            elif len(command2) > 8:
                return render(request, 'baakaa.html', {'output2': f'"{command2}" too much long'})
            elif command2.isdecimal():
                output2 = int(command2)*2
            else:
                try:
                    command2 = command2.replace("||"," ")
                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    # Set the working directory to the 'noob-player' folder
                    working_directory = os.path.join(current_directory, '..', 'noob-player')
                    output2 = subprocess.Popen(
                    ["/bin/bash", "-c", command2], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,cwd=working_directory)
                    output2 = output2.stdout.read().decode('utf-8')
                except Exception:
                    return render(request, 'baakaa.html', {'output2': f'Error executing command2: {command2}'})
        return render(request, 'baakaa.html', {'output1': output1,'output2':output2})
    return render(request, 'home.html')
