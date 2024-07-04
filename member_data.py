from threading import Lock
import discord

class SingeltonMeta():
    _instances = {}
    _lock: Lock = Lock()
    
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class MembersInVoiceData(SingeltonMeta):
    members_dict = {}

    # def __init__(self, member: discord.Member) -> None:
    #     if member.id not in self.members_dict:
    #         self.members_dict[member.id]['member'] = member

    def get_members_dict(self):
        return self.members_dict

    def add_member(self, member: discord.Member):
        member_to_add = self.members_dict.get(member.id, None)
        if not member_to_add:
            self.members_dict[member.id] = member

    def get_member(self, member: discord.Member):
        member_to_return = self.members_dict.get(member.id, None)
        if member_to_return:
            return member_to_return['member']
        return None

    def update_member(self, member: discord.Member):
        member_to_update = self.members_dict.get(member.id, None)
        if member_to_update:
            self.members_dict[member.id]['member'] = member

    def remove_member(self, member: discord.Member):
        member_to_remove = self.members_dict.get(member.id, None)
        if member_to_remove:
            del self.members_dict[member.id]