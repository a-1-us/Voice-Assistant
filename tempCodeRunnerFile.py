if __name__ == "__main__":
    music = Music()
    query = get_voice_query()
    if query:
        music.play(query)
    else:
        print("No valid voice input. Please try again.")