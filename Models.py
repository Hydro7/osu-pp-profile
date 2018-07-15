class Profile:
    def __init__(self):
        self.id = 0
        self.name = ''


class Score:
    def __init__(self):
        self.beatmap_hash = ''
        self.player_name = ''
        self.number_300s = 0
        self.number_100s = 0
        self.number_50s = 0
        self.gekis = 0
        self.katus = 0
        self.misses = 0
        self.score = 0
        self.max_combo = 0
        self.is_perfect_combo = False
        self.no_fail = False
        self.easy = False
        self.hidden = False
        self.hard_rock = False
        self.sudden_death = False
        self.double_time = False
        self.relax = False
        self.half_time = False
        self.flashlight = False
        self.spun_out = False
        self.auto_pilot = False
        self.perfect = False

    def __repr__(self):
        mods = []
        if self.no_fail:
            mods.append("NF")
        if self.easy:
            mods.append("EZ")
        if self.hidden:
            mods.append("HD")
        if self.hard_rock:
            mods.append("HR")
        if self.sudden_death:
            mods.append("SD")
        if self.double_time:
            mods.append("DT")
        if self.relax:
            mods.append("RX")
        if self.half_time:
            mods.append("HT")
        if self.flashlight:
            mods.append("FL")
        if self.spun_out:
            mods.append("SO")
        if self.auto_pilot:
            mods.append("AP")
        if self.perfect:
            mods.append("PF")
        mods_string = 'NoMod';
        if mods.count != 0:
            mods_string = ' '.join(mods)

        return 'Mods: {0}'.format(mods_string)