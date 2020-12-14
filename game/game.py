import pyfiglet 
from colorama import Fore, Back, Style  #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Style: DIM, NORMAL, BRIGHT, RESET_ALL
import gpt_2_simple as gpt2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def Play(a):

  file_name = "/content/AGT_rpg/Books/data.txt"

  g=pyfiglet.figlet_format("Generating world...", font = "slant")
  print(Fore.BLACK + Style.DIM)
  if  os.path.isdir("/content/AGT_rpg/models")== True:
    print("model exists")
  else:
    print("downloading model")
    gpt2.download_gpt2(model_name="774M")
  print(Fore.GREEN)
  print(Style.BRIGHT+g)
  print(Fore.BLACK + Style.DIM)
  sess = gpt2.start_tf_sess()

  gpt2.finetune(
      sess,
      dataset  = file_name,
      model_name = '774M',
      steps=700,
      restore_from='fresh',
      run_name = 'run1',
      print_every = 1,
      sample_every = 5000,
      save_every = 100         
                )

def loader(input1):
  print(Fore.GREEN)
  l=pyfiglet.figlet_format("Loading...", font = "slant")
  print(Style.BRIGHT+l)
  print(Fore.RESET)
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess)

  if input1 ==1:
    input1 = "I am "+'%Name'
  stories = gpt2.generate(sess,
                length=250,
                temperature=0.7,
                prefix=input1,
                nsamples=5,
                batch_size=5,
                top_k=40,
                run_name = 'run1',
                return_as_list=True
                )
    
  print(Fore.RESET + Style.RESET_ALL)
  story = ""
  temp = stories[3].split(".")
  del temp[-1]
  for i in temp:
    story = story +i+'.'
  return str(story)



def Menu(val,input1):
  print(Fore.MAGENTA)
  #print(Back.BLACK)
  result1 = pyfiglet.figlet_format("AGT", font = "isometric1") 
  result2 = pyfiglet.figlet_format(" rpg", font = "slant")
  print(Style.BRIGHT+result1+result2) 
  #Menu
  while True:
    inp=str(val)
    data = ""
    if inp=="1":
      if  os.path.isdir("/content/AGT_rpg/checkpoint/run1")== True:
        data = loader(input1)
      else:
        Play("1")
        data = loader(input1)
      return data
    elif inp=="3":
      exit()
    else:
      print("Enter a valid option")
