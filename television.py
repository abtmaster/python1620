class Television:
    """
    A class to show TV with features
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initialize TV with power off, muted off, volume and channel at minimum
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def channel_up(self):
        """
        Increase channel by one or reset to minimum if at max
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self):
        """
        Decrease channel by one or go to max if at minimum
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_down(self):
        """
        Decrease volume by one or unmute if currently muted
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1

    def volume_up(self):
        """
        Increase volume by one or unmute if currently muted
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1

    def mute(self):
        """
        Turn mute on or off
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def power(self):
        """
        Turn power on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def __str__(self):
        """
        Return a string showing power, channel and volume
        """
        if self.__muted:
            vol_display = 0
        else:
            vol_display = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {vol_display}'
