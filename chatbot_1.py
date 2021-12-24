import string
kabar = ['apa kabar', 'kabar', 'pie kabar',]
hallo = ['halo', 'hallo', 'p', 'guys','bro','sis']
chatbot_name = 'fitri' + 'bot'

while (True):
  user_massage = input('you: ').lower().strip(string.punctuation+string.whitespace)
  print (chatbot_name + ":", end=' ')

  if user_massage == 'quit' or user_massage == 'selesai':
    print ("sampai ketemu lagi")
    break

  if user_massage in hallo:
    print ('halo juga ', end='')
  elif user_massage == kabar:
    print ('baik nih , kamu gimana?', end='')
  elif 'cuaca cerah' in user_massage :
    print ('iyaa ,secerah hati ku', end='')
  elif 'mendung' in user_massage :
    print ('hati apa cuaca', end='')
  elif user_massage == 'hati':
    print ('hehe sabar ya', end='')
  elif user_massage == 'cuaca':
    print ('cuma cuaca kan hehe', end='')
  elif user_massage == 'cak':
    print ('pie cak', end='')
  elif user_massage == 'makasih' or user_massage == 'thanks':
    print ('masama', end='')
  else:
    print ('ehh gimana itu', end='')
  print()
