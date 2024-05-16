import streamlit as st
import numpy as np
import pandas as pd
from datasets import load_dataset

dataset = load_dataset("ITS-23-24/draft_nba")
df = pd.DataFrame(dataset['train'].to_dict()).set_index(['Year', 'Pick'])

def main():
    st.title('App Streamlit con Dataset')
    result = st.empty() #Aggiungi un'area di testo per visualizzare il risultato

    loc_player = np.random.choice(df.index) #scelta random di una riga del dataframe
    st.write(f"Da che team è stato draftato {df.loc[loc_player, 'Name']}")
    player_team = df.loc[loc_player, 'Team'] # salvo il team che ha scelto il giocatore al draft

    team_list = list(set(df['Team'])) #creo lista con tutti i team
    team_list.remove(player_team) #rimuovo dalla lista il team del giocatore scelto a caso

    shuffled_team_list = list(np.random.permutation(team_list)) #mescolo la lista dei team
    quiz_list = [player_team] #inizializzo la lista dei 4 team per il gioco mettendoci gia dentro il team del giocatore scelto

    for t in range(3): #scelta di altri 3 team per il gioco
        quiz_list.append(shuffled_team_list.pop())
    
    shuffled_quiz_list = np.random.permutation(quiz_list) #mescolo la lista per il gioco

    # Crea 4 bottoni
    button_1 = st.button(shuffled_quiz_list[0])
    button_2 = st.button(shuffled_quiz_list[1])
    button_3 = st.button(shuffled_quiz_list[2])
    button_4 = st.button(shuffled_quiz_list[3])

    button_list = [button_1, button_2, button_3, button_4]

    # Verifica quale bottone è stato cliccato e visualizza un messaggio appropriato
    if button_1:
        if shuffled_quiz_list[0] == player_team:
            result.success('Hai vinto!')
        else:
            result.success('Hai perso!')
    elif button_2:
        if shuffled_quiz_list[1] == player_team:
            result.success('Hai vinto!')
        else:
            result.success('Hai perso!')
    elif button_3:
        if shuffled_quiz_list[2] == player_team:
            result.success('Hai vinto!')
        else:
            result.success('Hai perso!')
    elif button_4:
        if shuffled_quiz_list[3] == player_team:
            result.success('Hai vinto!')
        else:
            result.success('Hai perso!')
   
if __name__ == '__main__':
    main()
