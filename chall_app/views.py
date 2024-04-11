from django.shortcuts import render
import subprocess
import os

def moshi(request):
    if request.method == 'POST':
        command1 = request.POST.get('command1', '')
        command2 = request.POST.get('command2', '')
        
        if command1:
            if any(c.isalpha() for c in command1):
                return render(request, 'baakaa.html', {'output1': f'{command1} Alphabets are not allowed in the command'})
            elif '. ./*/*' in command1:
                return render(request, 'baakaa.html', {'output1': f'{command1} Hehe not allowed'})
            else:
                try:
                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    # Set the working directory to the 'pro-player' folder
                    working_directory = os.path.join(current_directory, '..', 'pro-player')
                    output1 = subprocess.check_output(command1, shell=True, stderr=subprocess.STDOUT, cwd=working_directory, encoding='utf-8')
                    return render(request, 'baakaa.html', {'output1': output1.decode('utf-8')})
                except subprocess.CalledProcessError as e:
                    return render(request, 'baakaa.html', {'output1': f'Your 1st input is {command1}'})
                
        if command2:
            if any(c.isalpha() for c in command2):
                return render(request, 'baakaa.html', {'output2': f'{command2} Alphabets are not allowed in the command'})
            elif len(command2) >= 8:
                return render(request, 'baakaa.html', {'output2': f'{command2} too much long'})
            else:
                try:
                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    # Set the working directory to the 'noob-player' folder
                    working_directory = os.path.join(current_directory, '..', 'noob-player')
                    output2 = subprocess.check_output(command2, shell=True, stderr=subprocess.STDOUT,cwd=working_directory, encoding='utf-8')
                    return render(request, 'baakaa.html', {'output2': output2.decode('utf-8')})
                except subprocess.CalledProcessError as e:
                    return render(request, 'baakaa.html', {'output2': f'Your 2nd input is {command2}'})
                
    return render(request, 'home.html')
