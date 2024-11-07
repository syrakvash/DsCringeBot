from threading import Lock
import time
import discord

__REQ_COUNT__ = 4
__REQ_TIMEOUT__ = 100

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

    def __init_member__(self, member: discord.Member):
        self.members_dict[member.id] = {'member': member}
        self.members_dict[member.id]['reqs_history'] = []
        self.__reset_request_permission__(member.id)

    def add_member(self, member: discord.Member):
        member_to_add = self.members_dict.get(member.id, None)
        if not member_to_add:
            self.__init_member__(member)

    # def get_member(self, member: discord.Member):
    #     member_to_return = self.members_dict.get(member.id, None)
    #     if member_to_return:
    #         return member_to_return['member']
    #     return None

    def update_member(self, member: discord.Member):
        member_to_update = self.members_dict.get(member.id, None)
        if member_to_update:
            self.members_dict[member.id]['member'] = member

    def remove_member(self, member: discord.Member):
        member_to_remove = self.members_dict.get(member.id, None)
        if member_to_remove:
            del self.members_dict[member.id]

    def get_member_request_history(self, member: discord.Member):
        member_to_get_history = self.members_dict.get(member.id, None)
        return member_to_get_history['reqs_history']
    
    def update_member_request_history(self, member: discord.Member, request, response):
        member_to_update_history = self.members_dict.get(member.id, None)
        member_to_update_history['reqs_history'] += [
            {'role': 'user', 'content': request},
            {'role': 'assistant', 'content': response}
            ]

    def check_request_permission(self, member:discord.Member):
        member_to_cringe_request = self.members_dict.get(member.id, None)
        if member_to_cringe_request:
            if self.members_dict[member.id]['req_count'] == 0:
                self.members_dict[member.id]['req_first_time'] = time.time()
            self.members_dict[member.id]['req_count'] += 1
            get_delta_time = time.time() - self.members_dict[member.id]['req_first_time']
            req_count = self.members_dict[member.id]['req_count']
            if req_count >= __REQ_COUNT__:
                if get_delta_time < __REQ_TIMEOUT__:
                    self.members_dict[member.id]['req_permission'] = False
                    print(f'Member {member.id} banned, reqs count: {req_count}')
                else:
                    self.__reset_request_permission__(member.id)
            return self.members_dict[member.id]['req_permission']
        
    def __reset_request_permission__(self, member_id):
        self.members_dict[member_id]['req_count'] = 0
        self.members_dict[member_id]['req_first_time'] = time.time()
        self.members_dict[member_id]['req_permission'] = True
        print(f'Member {member_id} initialised/released from ban')
