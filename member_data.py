from threading import Lock
import time
import discord

__CRINGE_REQ_COUNT__ = 3
__CRINGE_REQ_TIMEOUT__ = 80

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

    def get_members_dict(self):
        return self.members_dict

    def add_member(self, member: discord.Member):
        member_to_add = self.members_dict.get(member.id, None)
        if not member_to_add:
            self.members_dict[member.id] = {'member': member}

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

    def cringe_request(self, member:discord.Member):
        member_to_cringe_request = self.members_dict.get(member.id, None)
        if member_to_cringe_request:
            if 'cringe_req_count' not in self.members_dict[member.id]:
                self.__reset_cringe_request__(member.id)
            else:
                self.members_dict[member.id]['cringe_req_count'] += 1
            get_delta_time = time.time() - self.members_dict[member.id]['cringe_first_time']
            cringe_req_count = self.members_dict[member.id]['cringe_req_count']
            if cringe_req_count >= __CRINGE_REQ_COUNT__:
                if get_delta_time < __CRINGE_REQ_TIMEOUT__:
                    self.members_dict[member.id]['cringe_allowed'] = False
                    print(f'Member {member.id} banned, cringe reqs number: {cringe_req_count}')
                else:
                    self.__reset_cringe_request__(member.id)
                
            return self.members_dict[member.id]['cringe_allowed']
        
    def __reset_cringe_request__(self, member_id):
        self.members_dict[member_id]['cringe_req_count'] = 0
        self.members_dict[member_id]['cringe_first_time'] = time.time()
        self.members_dict[member_id]['cringe_allowed'] = True
        print(f'Member {member_id} initialised/released from ban')
