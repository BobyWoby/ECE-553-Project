# Source before running legacy Maze2D on this host; no system files are modified.
export PATH="$HOME/eecs553/.venv/bin:$HOME/eecs553/tools/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.mujoco/mujoco210/bin:/usr/lib/nvidia:/usr/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export C_INCLUDE_PATH="$HOME/eecs553/tools/include${C_INCLUDE_PATH:+:$C_INCLUDE_PATH}"
export CFLAGS='-O2 -std=gnu11 -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration -Wno-error=int-conversion'
export MUJOCO_GL=egl
