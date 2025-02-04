from gym.envs.registration import register
import os.path as osp
from randomizer.safe_env.pendulum.safe_pendulum import pendulum_cfg, SafePendulumEnv, SautedPendulumEnv
from randomizer.safe_env.double_pendulum.safe_double_pendulum import double_pendulum_cfg, SafeDoublePendulumEnv, \
    RandomizeSafeDoublePendulumEnv
from randomizer.safe_env.safe_fetch_slide.safe_fetch_slide import SafeFetchSlideEnv

print('LOADING SAFE ENVIROMENTS')

register(
    id='SafePendulum-v0',
    entry_point='randomizer.safe_env.pendulum.safe_pendulum:SafePendulumEnv',
    max_episode_steps=pendulum_cfg['max_ep_len'],
    # max_episode_steps=200,
)

register(
    id='SafeDoublePendulum-v0',
    entry_point='randomizer.safe_env.double_pendulum.safe_double_pendulum:SafeDoublePendulumEnv',
    max_episode_steps=double_pendulum_cfg['max_ep_len'],
    # max_episode_steps=200,
)

register(
    id='RandomizeSafeDoublePendulum-v0',
    entry_point='randomizer.safe_env.double_pendulum.safe_double_pendulum:RandomizeSafeDoublePendulumEnv',
    max_episode_steps=200,
)
register(
    id='SafeFetchSlide-v0',
    entry_point='randomizer.safe_env.safe_fetch_slide.safe_fetch_slide:SafeFetchSlideEnv',
    max_episode_steps=50,
)

register(
    id='SafeFetchSlideWithCostFn-v0',
    entry_point='randomizer.safe_env.safe_fetch_slide.randomized_safe_fetch_slide_with_cost:SafeFetchSlideWithCost',
    max_episode_steps=50,
)

register(
    id='RandomizeSafeFetchSlideCostEnv-v0',
    entry_point='randomizer.safe_env.safe_fetch_slide.randomized_safe_fetch_slide_with_cost:RandomizeSafeFetchSlideCostEnv',
    max_episode_steps=50,
)

register(
    id='LunarLanderDefault-v0',
    entry_point='randomizer.lunar_lander:LunarLanderRandomized',
    max_episode_steps=1000,
    kwargs={'config': 'randomizer/config/LunarLanderRandomized/default.json'}
)

register(
    id='LunarLanderRandomized-v0',
    entry_point='randomizer.lunar_lander:LunarLanderRandomized',
    max_episode_steps=1000,
    kwargs={'config': 'randomizer/config/LunarLanderRandomized/random.json'}
)

register(
    id='Pusher3DOFDefault-v0',
    entry_point='randomizer.pusher3dof:PusherEnv3DofEnv',
    max_episode_steps=100,
    kwargs={'config': 'randomizer/config/Pusher3DOFRandomized/default.json'}
)

register(
    id='Pusher3DOFRandomized-v0',
    entry_point='randomizer.pusher3dof:PusherEnv3DofEnv',
    max_episode_steps=100,
    kwargs={'config': 'randomizer/config/Pusher3DOFRandomized/random.json'}
)

register(
    id='HumanoidRandomizedEnv-v0',
    entry_point='randomizer.humanoid:HumanoidRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/HumanoidRandomized/default.json',
        'xml_name': 'humanoid.xml'
    }
)

register(
    id='HalfCheetahRandomizedEnv-v0',
    entry_point='randomizer.half_cheetah:HalfCheetahRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/HalfCheetahRandomized/default.json',
        'xml_name': 'half_cheetah.xml'
    }
)

register(
    id='FetchPushRandomizedEnv-v0',
    entry_point='randomizer.randomized_fetchpush:FetchPushRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/FetchPushRandomized/default.json',
        'xml_name': 'push.xml'
    }
)
register(
    id='ResidualPushRandomizedEnv-v0',
    entry_point='randomizer.randomized_residual_push:ResidualPushRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualPushRandomized/random.json',
        'xml_name': 'push.xml'
    }
)
register(
    id='ResidualPushDefaultEnv-v0',
    entry_point='randomizer.randomized_residual_push:ResidualPushRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualPushRandomized/default.json',
        'xml_name': 'push.xml'
    }
)

register(
    id='ResidualPickAndPlaceRandomizedEnv-v0',
    entry_point='randomizer.randomized_pick_and_place:ResidualPickAndPlaceRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualPickAndPlaceRandomized/random.json',
        'xml_name': 'pick_and_place.xml'
    }
)
register(
    id='ResidualPickAndPlaceDefaultEnv-v0',
    entry_point='randomizer.randomized_pick_and_place:ResidualPushRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualPickAndPlaceRandomized/default.json',
        'xml_name': 'pick_and_place.xml'
    }
)
register(
    id='ResidualMPCPushRandomizedEnv-v0',
    entry_point='randomizer.randomized_mpc_push:ResidualMPCPushRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualMPCPushRandomized/random.json',
        'xml_name': 'push.xml'
    }
)
register(
    id='ResidualMPCPushDefaultEnv-v0',
    entry_point='randomizer.randomized_mpc_push:ResidualMPCPushRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualMPCPushRandomized/default.json',
        'xml_name': 'push.xml'
    }
)

register(
    id='FetchHookRandomizedEnv-v0',
    entry_point='randomizer.randomized_fetch_hook:RandomizedFetchHookEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualFetchHookRandomized/random.json',
        'xml_name': 'hook.xml'
    }
)
register(
    id='FetchHookDefaultEnv-v0',
    entry_point='randomizer.randomized_fetch_hook:RandomizedFetchHookEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualFetchHookRandomized/default.json',
        'xml_name': 'hook.xml'
    }
)
register(
    id='ResidualHookRandomizedEnv-v0',
    entry_point='randomizer.randomized_residual_hook:ResidualFetchHookEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualFetchHookRandomized/random.json',
        'xml_name': 'hook.xml'
    }
)
register(
    id='ResidualHookDefaultEnv-v0',
    entry_point='randomizer.randomized_residual_hook:ResidualFetchHookEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/ResidualFetchHookRandomized/default.json',
        'xml_name': 'hook.xml'
    }
)

register(
    id='ResidualNoisyHookRandomizedEnv-v0',
    entry_point='randomizer.randomized_residual_hook:TwoFrameResidualHookNoisyEnv',
    max_episode_steps=100,
    kwargs={
        'config': 'randomizer/config/ResidualFetchHookRandomized/random.json',
        'xml_name': 'hook.xml'
    }
)
register(
    id='ResidualNoisyHookDefaultEnv-v0',
    entry_point='randomizer.randomized_residual_hook:TwoFrameResidualHookNoisyEnv',
    max_episode_steps=100,
    kwargs={
        'config': 'randomizer/config/ResidualFetchHookRandomized/default.json',
        'xml_name': 'hook.xml'
    }
)

register(
    id='AntRandomizedEnv-v0',
    entry_point='randomizer.ant:AntRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/AntRandomized/default.json',
        'xml_name': 'ant.xml'
    }
)

register(
    id='ReacherRandomizedEnv-v0',
    entry_point='randomizer.reacher:ReacherRandomizedEnv',
    max_episode_steps=50,
    kwargs={
        'config': 'randomizer/config/ReacherRandomized/default.json',
        'xml_name': 'reacher.xml'
    }
)

register(
    id='InvertedDoublePendulumRandomizedEnv-v0',
    entry_point='randomizer.inverted_double_pendulum:InvertedDoublePendulumRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/InvertedDoublePendulumRandomized/default.json',
        'xml_name': 'inverted_double_pendulum.xml'
    }
)
register(
    id='InvertedPendulumRandomizedEnv-v0',
    entry_point='randomizer.inverted_pendulum:InvertedPendulumRandomizedEnv',
    max_episode_steps=1000,
    kwargs={
        'config': 'randomizer/config/InvertedPendulumRandomized/default.json',
        'xml_name': 'inverted_pendulum.xml'
    }
)