from emath.main import prefix_emojis
import emath


def test_parse():
    data, emojis = emath.get_data()
    prefixed = prefix_emojis('👑', emojis)
    assert 'emoji2vec' in prefixed
    prefixed = prefix_emojis('np.sin(🏰)', emojis)
    assert prefixed == 'np.sin(emoji2vec["🏰"])'


def test_exec_emojis():
    data, emojis = emath.get_data()
    result = emath.exec_emojis('👑 - 🚹 + 🚺', data, emojis)
    result = emath.exec_emojis('🚹 @ 🚺', data, emojis)
    result = emath.exec_emojis('np.sin(🏰)', data, emojis)
    result = emath.exec_emojis('🚹**2', data, emojis)
