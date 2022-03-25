import disnake

async def invalid_user_response(interaction):
    embed = disnake.Embed(description="Sorry, the command was executed by another user")
    await interaction.response.send_message(embed=embed,  ephemeral=True)

class Create:
    def __init__(
            self,
            segments,
            title="",
            color=0x000000,
            prefix="",
            suffix="",
            target_page=1,
            timeout=300,
            button_style=disnake.ButtonStyle.gray,
            invalid_user_function=invalid_user_response,
        ):
        self.embeds = []
        self.current_page = target_page
        self.timeout = timeout
        self.button_style = button_style
        self.invalid_user_function = invalid_user_function

        for segment in segments:
            if isinstance(segment, disnake.Embed):
                self.embeds.append(segment)
            else:
                self.embeds.append(
                    disnake.Embed(
                        title=title,
                        color=color,
                        description=prefix + segment + suffix,
                    ),
                )

        if self.current_page > len(segments) or self.current_page < 1:
            self.current_page = 1

        class PaginatorView(disnake.ui.View):
            def __init__(this, interaction):
                super().__init__()
                
                this.timeout = self.timeout
                this.interaction = interaction

            async def on_timeout(this):
                for button in this.children:
                    button.disabled = True
                await this.interaction.edit(embed=self.embeds[self.current_page-1], view=this)
                return await super().on_timeout()

            def update_page(this):
                for button in this.children:
                    if button.label:
                        if button.label.strip() != "":
                            button.label = f"{self.current_page}/{len(self.embeds)}"


            @disnake.ui.button(emoji="⬅️",label="Previous", style=self.button_style, disabled=True if len(self.embeds) == 1 else False)
            async def previous_button(this, _, button_interaction):
                if button_interaction.author != this.interaction.author:
                    await self.invalid_user_function(button_interaction)
                    return

                self.current_page -= 1
                if self.current_page < 1:
                    self.current_page = len(self.embeds)
                this.update_page()
                await button_interaction.response.edit_message(embed=self.embeds[self.current_page-1], view=this)

            @disnake.ui.button(label=f"{self.current_page}/{len(self.embeds)}", style=disnake.ButtonStyle.gray, disabled=True)
            async def page_button(*_):
                pass

            @disnake.ui.button(emoji="➡️",label="Next", style=self.button_style, disabled=True if len(self.embeds) == 1 else False)
            async def next_button(this, _, button_interaction):
                if button_interaction.author != this.interaction.author:
                    await self.invalid_user_function(button_interaction)
                    return

                self.current_page += 1
                if self.current_page > len(self.embeds):
                    self.current_page = 1
                this.update_page()
                await button_interaction.response.edit_message(embed=self.embeds[self.current_page-1], view=this)


    async def start(self, interaction, ephemeral=False, deferred=False,replied=True):
        if not deferred:
            if not replied:
            	await interaction.send(embed=self.embeds[self.current_page-1], view=self.view(interaction))
            else:
            	await interaction.reply(embed=self.embeds[self.current_page-1], view=self.view(interaction))
        else:
            await interaction.edit_original_message(embed=self.embeds[self.current_page-1], view=self.view(interaction))
