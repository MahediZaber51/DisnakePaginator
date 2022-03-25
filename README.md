# EasyDisnakePaginator
A package containing easy paginator for disnake

## Examples
Creating a Paginator without embeds:
```py
paginator = EasyDisnakePaginator.Create(title="Easy Disnake Paginator", segments=["1st message", "2nd messagge"], color=0x00ff00)
await paginator.start(ctx)

```

Creating a Paginator with embeds
```py
paginator = EasyDisnakePaginator.Create(title="Easy Disnake Paginator", segments=[embed1, embed2], color=0x00ff00)
await paginator.start(ctx)
```

## Arguments
`title` = The title of the embed (when the segments are `str`) [type:`str`]\
\
`segments` = The pages of the paginator (supports `str` and `disnake.Embed`) [type: `str` or `disnake.Embed`]]\
\
`color` = The color of the embed\
\
`prefix` = The prefix text of every page in the embed (when the segments are `str`) [type: `str`]\
\
`suffix` = The suffix text of every page in the embed (when the segments are `str`) [type:`str`]\
\
`target_page` = The page that the paginator will display when created [type: `int`]\
\
`timeout` = The amount of seconds after the paginator buttons will stop working [type: `int`]\
\
`button_style` = The style of the buttons on the paginator [type: `disnake.ButtonStyle`]\
\
`invalid_user_function` = The function that will be called when another user tries to use the paginator. By default it will show an embed unless any function is specified.[type `function`]
## Useful Links:
**[WEBSITE](https://zealtyro.com)**\
**[YOUTUBE](https://youtube.com/ZealTyro)**\
**[TWITTER](https://twitter.com/MahediZaber)**
