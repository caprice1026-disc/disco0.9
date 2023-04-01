import discord
import app_commands
import os

os.getenv('KEY')
TOKEN = "KEY"

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
prefix = "/"
#鯖設定するなら　guild = discord.guild(id=)
class confomationview(discord.ui.View):
    def __init__(self, interaction: discord.Interaction, timeout=60, text=""):
        super().__init__(timeout=timeout)
        self.send_embed = discord.Embed(title="新作の宣伝です！", description=text)
        self.send_embed.set_author(
           name=interaction.user.display_name, 
           icon_url=interaction.user.display_avatar.url, 
        ).set_footer(
           text=f"transfar from {interaction.user.display_name}",
           icon_url=interaction.user.display_avatar.url,
        )
        #チャンネルID書き換えること
        self.channel = client.get_channel()
    @discord.ui.button(label="OK", style=discord.ButtonStyle.success)
    async def ok(self, button: discord.ui.Button, interaction: discord.Interaction):
        #Embedの中身を指定すること
        await self.channel.send(embed=self.send_embed)
        pass
    @discord.ui.button(label="NG", style=discord.ButtonStyle.gray)
    async def ng(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass
    
@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()
@tree.command(name="promotion",description="アクティブクリエイターが宣伝するためのコマンドです。")
@app_commands.describe(role="誰に送るかを指定。",text="送りたい文章を書き込んでください。")
async def promotion_command(interaction: discord.Interaction,role: discord.Role,text: str):
    #ここで一回確認を取りたい　フォローアップ関数だとエラーを吐く
    #rolenameの定義の仕方(問題なし)
    rolename = role
    view = confomationview(interaction=interaction, text=text,)
    await interaction.response.send_message(f"{rolename}へ{text}  と送信してよいですか？", ephemeral=True)
    await interaction.followup.send(view=view, ephemeral=True) 

client.run(TOKEN)


