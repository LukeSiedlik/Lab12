class Television:
    """
    A class representing a Television with power, mute, channel, and volume functionality.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the Television with default settings:
        Power off, not muted, volume at MIN_VOLUME, and channel at MIN_CHANNEL.
        All methods should only work if the television is powered on
        Except the power on function itself
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the Television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status if the Television is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel by 1, wrapping to MIN_CHANNEL if at MAX_CHANNEL.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by 1, wrapping to MAX_CHANNEL if at MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1 up to MAX_VOLUME.
        Automatically unmutes if the Television is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 down to MIN_VOLUME.
        Automatically unmutes if the Television is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns the current state of the Television as a string.
        If muted, volume is displayed as 0.
        Returns: formatted string with power, channel, and volume status.
        """
        volume_display: int = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"
