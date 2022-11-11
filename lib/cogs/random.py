import requests
from multiprocessing.pool import ThreadPool as Pool
from discord.ext import commands
import discord

import sys
sys.path.append("lib")
from utilities.check_image_url import check_image_url
from utilities.get_random_prntsc import get_random_prntsc
from utilities.get_soup import get_soup

global images
images = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}


            

def check_valid(prntsc_url: str) -> None:
    # Init session
    with requests.Session() as session:
        # Init headers
        session.headers = headers
        
        soup = get_soup(prntsc_url, session=session)
        img = check_image_url(soup, session)
        
        if img is not None:
            images.append(img)
        else:
            pass
    
def generate_images():
    
    pool = Pool(4)
    for _ in range(4):
        url = get_random_prntsc()
        pool.apply_async(check_valid,( url,))
        
    pool.close()
    pool.join()
            
    
class Prntsc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


        @self.bot.tree.command(name="random", description="Random image from prntsc")
        async def random(interaction: discord.Interaction):
    
            if len(images) == 0:
                generate_images()
                print(len(images))
                
                await interaction.response.send_message(images[0])
                images.remove(images[0])
                generate_images()
                
            else:
                await interaction.response.send_message(images[0])
                images.remove(images[0])
                generate_images()
                
                
async def setup(bot):
    await bot.add_cog(Prntsc(bot))