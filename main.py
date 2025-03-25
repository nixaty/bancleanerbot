from bot import bot
import logging
import handlers


if __name__ == "__main__":
    from os import makedirs
    makedirs("data", exist_ok=True)

    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                        filename='data/bot.log', 
                        filemode='w'
                        )
    bot.run()
