from iconservice import *

TAG = 'BissScore'

class BissScore(IconScoreBase):

    _DATASTORAGE = 'datastorage'
    _FIRMWARES = 'firmwares'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self._datastorage = ArrayDB(self._DATASTORAGE, db, value_type=dict)
        self._firmwares = DictDB(self._FIRMWARES, db, value_type=bytes)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @payable
    def fallback(self):
        Logger.info('fallback is called', TAG)

    @external
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        Logger.info('tokenFallabck is called', TAG)
    
    @external(readonly=True)
    def name(self) -> str:
        return 'BissScore'

    @external(readonly=True)
    def get_firmware(self, _fileId) -> dict:
        '''Get firmware dict with file_id'''

        return self._firmwares[_fileID]

    @external
    def save_data(_data: dict):
        '''store data from device'''

        idx = len(self._datastorage)
        self._datastorage.push(_data)
        Logger.debug('data[{}]: {}'.format(
            idx,
            json_dumps(_data)
        ), TAG)

    @external
    def save_hash(_fileId: int, _hash: str):
        '''Store firmware hash for file id'''
        
        firmware = self.get_firmware(_fileId)
        if firmware and not firmware['hash']:
            self.firmwares['hash'] = _hash
        else:
            self.firmwares[_fileId] = {
                'key': None,
                'hash': _hash
            }
            firmware = self.get_firmware(_fileId)
        Logger.debug('firmware[{}]: {}'.format(
            _fileId,
            json_dumps(firmware)
        ), TAG)

    @external
    def save_key(_fileId: int, _key: str):
        '''Store firmware key for file id'''

        firmware = self.get_firmware(_fileId)
        if firmware and not firmware['key']:
            self.firmwares[_fileID]['key'] = _key
        else:
            self.firmwares[_fileId] = {
                'key': None,
                'hash': _key
            }
            firmware = self.get_firmware(_fileId)
        Logger.debug('firmware[{}]: '.format(_fileId) + json_dumps(firmware), TAG)

    @external(readonly=True)
    def verify_hash(self, _fileId, _hash) -> bool:
        '''Verify firmware hash'''

        firmware = self.get_firmware(_fileId)
        return firmware['hash'] == _hash
