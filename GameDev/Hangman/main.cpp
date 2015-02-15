#ifdef _MSC_VER  
	#ifdef _WIN32
		#ifndef _DEBUG
			#pragma comment( lib, "sfml-system.lib" )		
			#pragma comment( lib, "sfml-graphics.lib" )			
			#pragma comment( lib, "sfml-window.lib" )	
		#else
			#pragma comment( lib, "sfml-system-d.lib" )		
			#pragma comment( lib, "sfml-graphics-d.lib" )			
			#pragma comment( lib, "sfml-window-d.lib" )	
		#endif
	#endif
#endif

#include <SFML\Graphics.hpp>
#include <array>
#include "../common/common.h"



class HangmanGame : public GameCore
{
public:
    HangmanGame(int width, int height, const sf::String & name) : GameCore(width, height, name)
    {
    }

    void gameEvent()
    {
        sf::Event event;
        while(gameWindow.pollEvent(event))
        {
            if (isQuitRequested(event))
                gameWindow.close();
            else
            {
                if (event.type == sf::Event::TextEntered)
                {
                    char c = static_cast<char> (event.text.unicode);
                    if (c >= 'a' && c <= 'z' )
                    {
                        textEntered += event.text.unicode;
                        enter.setString (textEntered); //update the enter Text
                        
                        bgSprite.setTexture(textures[++errorNumber]);	

                    }
                    
                }
            }
        }
    }
    

    void gameLoop()
    {
        while(gameWindow.isOpen())
        {
            gameWindow.clear(sf::Color(0, 0, 0));

            if (isGameOn)
            {
                gameWindow.draw(bgSprite);
                gameWindow.draw(question);
                gameWindow.draw(enter);

            }
            else
            {
                if (hasPlayerWon)
                    gameWindow.draw(won);
                else
                    gameWindow.draw(lost);                    
            }
            gameWindow.display();
            gameEvent();            
        }

    }

    int setup()
    {
        errorNumber = 0;
        const int spriteWidth = 640;
        const int spriteHeight = 380;
        int i = 0;
        for(auto & text : textures)
        {
            if (!text.loadFromFile("../resource/graphics/hangman/hangman_" + toString(i) + ".png", sf::IntRect(0, 0, spriteWidth, spriteHeight)))
            {	
                return EXIT_FAILURE;
            }
            ++i;
        }

        textEntered = "";

        bgSprite.setTexture(textures[errorNumber]);	
        bgSprite.setPosition(0, 0);
        
        
        if (!font.loadFromFile("../resource/tomb.ttf"))
            return EXIT_FAILURE;   

        question = sf::Text("Guess a letter of the word?", font, 16);
        question.setPosition(10,390);
        question.setColor(sf::Color::Green);

        enter = sf::Text("", font, 16);
        enter.setPosition(10, 420);
        enter.setColor(sf::Color::Red);

        won = sf::Text("You have discovered\n the secret word\n in less than 10 tries,\n well played !", font, 20);
        won.setPosition(5, 70);
        won.setColor(sf::Color::Green);

        lost = sf::Text("You have failed to\n discover the secret\n number in less than\n 10 tries, better \nluck next time!", font, 20);
        lost.setPosition(5, 70);
        lost.setColor(sf::Color::Red);

        isGameOn = true;
        hasPlayerWon = false;

        return EXIT_SUCCESS;

    }
private:

    int errorNumber;
    std::array<sf::Texture, 9> textures;
    sf::Sprite bgSprite;
    
    sf::Font font; 

    sf::Text question;
    sf::Text enter;
    sf::Text won;
    sf::Text lost;
    sf::String textEntered;

    bool isGameOn;
    bool hasPlayerWon;
};


int main()
{
    HangmanGame game(640, 480, "Hangman Game");
    if (game.setup() != EXIT_SUCCESS)
        return EXIT_FAILURE;
    game.gameLoop();
    return EXIT_SUCCESS;
}




  
