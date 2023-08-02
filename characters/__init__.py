class Combatant():
    """
    """


    health = 0
    max_health = 0
    image = ''
    name = ''

    def health_bar(self):
        """
        """


        health_ratio = int(self.health / self.max_health * 25)
        title = self.image.capitalize()
        if self.image != self.name:
            title += ' / ' + self.name.capitalize()
        bar = '=' * health_ratio + ' ' * (health_ratio - 25)
        info = 'Health: ' + ' ' * (4 - len(str(self.health))) + str(self.health) + ' / ' \
            + ' ' * (4 - len(str(self.max_health))) + str(self.max_health)
        print(title)
        print(bar)
        print(info)
