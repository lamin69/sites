[DEBUG]:   	ERROR: Ignored the following yanked versions: 1.2.9.post1
[DEBUG]:   	ERROR: Could not find a version that satisfies the requirement pysmb==1.2.9 (from versions: 1.0.0a0, 1.0.1, 1.0.2, 1.0.3, 1.0.4, 1.0.5, 1.1.0, 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6, 1.1.7, 1.1.8, 1.1.9, 1.1.10, 1.1.11, 1.1.12, 1.1.13, 1.1.14, 1.1.15, 1.1.16, 1.1.17, 1.1.18, 1.1.19, 1.1.20, 1.1.21, 1.1.22, 1.1.23, 1.1.24, 1.1.25, 1.1.26, 1.1.27, 1.1.28, 1.1.29, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7, 1.2.8, 1.2.9.1)
[DEBUG]:   	ERROR: No matching distribution found for pysmb==1.2.9
[DEBUG]:   	
Exception in thread background thread for pid 190788:
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 1641, in wrap
    fn(*rgs, **kwargs)
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 2569, in background_thread
    handle_exit_code(exit_code)
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 2269, in fn
    return self.command.handle_command_exit_code(exit_code)
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 869, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_1: 

  RAN: /usr/bin/bash -c 'venv/bin/pip install -v --target '"'"'/content/.buildozer/android/platform/build-arm64-v8a/build/python-installs/lamineft/arm64-v8a'"'"' --no-deps -r requirements.txt'

  STDOUT:
Ignoring "sys._home = value" override
Using pip 24.1.1 from /content/.buildozer/android/platform/build-arm64-v8a/build/venv/lib/python3.11/site-packages/pip (python 3.11)
Collecting certifi (from -r requirements.txt (line 1))
  Obtaining dependency information for certifi from https://files.pythonhosted.org/packages/1c/d5/c84e1a17bf61d4df64ca866a1c9a913874b4e9bdc131ec689a0ad013fb36/certifi-2024.7.4-py3-none-any.whl.metadata
  Using cached certifi-2024.7.4-py3-none-any.whl.metadata (2.2 kB)
Collecting chardet (from -r requirements.txt (line 2))
  Obtaining dependency information for chardet from https://files.pythonhosted.org/packages/38/6f/f5fbc992a329ee4e0f288c1fe0e2ad9485ed064cac731ed2fe47dcc38cbf/chardet-5.2.0-py3-none-any.whl.metadata
  Using cached chardet-5.2.0-py3-none-any.whl.metadata (3.4 kB)
Collecting idna (from -r requirements.txt (line 3))
  Obtaining dependency information for idna from https://files.pythonhosted.org/packages/e5/3e/741d8c82801c347547f8a2a06aa57dbb1992be9e948df2ea0eda2c8b79e8/idna-3.7-py3-none-any.whl.metadata
  Using cached idna-3.7-py3-none-any.whl.metadata (9.9 kB)
Collecting paramiko==3.3.1 (from -r requirements.txt (line 4))
  Obtaining dependency information for paramiko==3.3.1 from https://files.pythonhosted.org/packages/bb/8f/3cef65d3fe76e59f320405027d594a0332e44852fef722f0ee4e81e2e7e3/paramiko-3.3.1-py3-none-any.whl.metadata
  Downloading paramiko-3.3.1-py3-none-any.whl.metadata (4.4 kB)
Collecting plyer==2.1.0 (from -r requirements.txt (line 5))
  Obtaining dependency information for plyer==2.1.0 from https://files.pythonhosted.org/packages/d3/89/a41c2643fc8eabeb84791acb9d0e4d139b1e4b53473cc4dae947b5fa33ed/plyer-2.1.0-py2.py3-none-any.whl.metadata
  Using cached plyer-2.1.0-py2.py3-none-any.whl.metadata (61 kB)
ERROR: Ignored the following yanked versions: 1.2.9.post1
ERROR: Could not find a version that satisfies the requirement pysmb==1.2.9 (from versions: 1.0.0a0, 1.0.1, 1.0.2, 1.0.3, 1.0.4, 1.0.5, 1.1.0, 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6, 1.1.7, 1.1.8, 1.1.9, 1.1.10, 1.1.11, 1.1.12, 1.1.13, 1.1.14, 1.1.15, 1.1.16, 1.1.17, 1.1.18, 1.1.19, 1.1.20, 1.1.21, 1.1.22, 1.1.23, 1.1.24, 1.1.25, 1.1.26, 1.1.27, 1.1.28, 1.1.29, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7, 1.2.8, 1.2.9.1)
ERROR: No matching distribution found for pysmb==1.2.9


  STDERR:

Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 1256, in <module>
    main()
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/entrypoints.py", line 18, in main
    ToolchainCL()
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 685, in __init__
    getattr(self, command)(args)
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 104, in wrapper_func
    build_dist_from_args(ctx, dist, args)
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 163, in build_dist_from_args
    build_recipes(build_order, python_modules, ctx,
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/build.py", line 528, in build_recipes
    run_pymodules_install(
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/build.py", line 757, in run_pymodules_install
    shprint(sh.bash, '-c', (
  File "/content/.buildozer/android/platform/python-for-android/pythonforandroid/logger.py", line 167, in shprint
    for line in output:
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 915, in next
    self.wait()
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 845, in wait
    self.handle_command_exit_code(exit_code)
  File "/root/.local/lib/python3.10/site-packages/sh.py", line 869, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_1: 

  RAN: /usr/bin/bash -c 'venv/bin/pip install -v --target '"'"'/content/.buildozer/android/platform/build-arm64-v8a/build/python-installs/lamineft/arm64-v8a'"'"' --no-deps -r requirements.txt'

  STDOUT:
Ignoring "sys._home = value" override
Using pip 24.1.1 from /content/.buildozer/android/platform/build-arm64-v8a/build/venv/lib/python3.11/site-packages/pip (python 3.11)
Collecting certifi (from -r requirements.txt (line 1))
  Obtaining dependency information for certifi from https://files.pythonhosted.org/packages/1c/d5/c84e1a17bf61d4df64ca866a1c9a913874b4e9bdc131ec689a0ad013fb36/certifi-2024.7.4-py3-none-any.whl.metadata
  Using cached certifi-2024.7.4-py3-none-any.whl.metadata (2.2 kB)
Collecting chardet (from -r requirements.txt (line 2))
  Obtaining dependency information for chardet from https://files.pythonhosted.org/packages/38/6f/f5fbc992a329ee4e0f288c1fe0e2ad9485ed064cac731ed2fe47dcc38cbf/chardet-5.2.0-py3-none-any.whl.metadata
  Using cached chardet-5.2.0-py3-none-any.whl.metadata (3.4 kB)
Collecting idna (from -r requirements.txt (line 3))
  Obtaining dependency information for idna from https://files.pythonhosted.org/packages/e5/3e/741d8c82801c347547f8a2a06aa57dbb1992be9e948df2ea0eda2c8b79e8/idna-3.7-py3-none-any.whl.metadata
  Using cached idna-3.7-py3-none-any.whl.metadata (9.9 kB)
Collecting paramiko==3.3.1 (from -r requirements.txt (line 4))
  Obtaining dependency information for paramiko==3.3.1 from https://files.pythonhosted.org/packages/bb/8f/3cef65d3fe76e59f320405027d594a0332e44852fef722f0ee4e81e2e7e3/paramiko-3.3.1-py3-none-any.whl.metadata
  Downloading paramiko-3.3.1-py3-none-any.whl.metadata (4.4 kB)
Collecting plyer==2.1.0 (from -r requirements.txt (line 5))
  Obtaining dependency information for plyer==2.1.0 from https://files.pythonhosted.org/packages/d3/89/a41c2643fc8eabeb84791acb9d0e4d139b1e4b53473cc4dae947b5fa33ed/plyer-2.1.0-py2.py3-none-any.whl.metadata
  Using cached plyer-2.1.0-py2.py3-none-any.whl.metadata (61 kB)
ERROR: Ignored the following yanked versions: 1.2.9.post1
ERROR: Could not find a version that satisfies the requirement pysmb==1.2.9 (from versions: 1.0.0a0, 1.0.1, 1.0.2, 1.0.3, 1.0.4, 1.0.5, 1.1.0, 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6, 1.1.7, 1.1.8, 1.1.9, 1.1.10, 1.1.11, 1.1.12, 1.1.13, 1.1.14, 1.1.15, 1.1.16, 1.1.17, 1.1.18, 1.1.19, 1.1.20, 1.1.21, 1.1.22, 1.1.23, 1.1.24, 1.1.25, 1.1.26, 1.1.27, 1.1.28, 1.1.29, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7, 1.2.8, 1.2.9.1)
ERROR: No matching distribution found for pysmb==1.2.9


  STDERR:




# Command failed: ['/usr/bin/python3', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=lamineft', '--bootstrap=sdl2', '--requirements=python3,kivy==2.2.1,plyer==2.1.0,android==1.0.0,paramiko==3.3.1,webdavclient3==3.14.6,pysmb==1.2.9', '--arch=arm64-v8a', '--copy-libs', '--color=always', '--storage-dir=/content/.buildozer/android/platform/build-arm64-v8a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# ENVIRONMENT:
#     SHELL = '/bin/bash'
#     NV_LIBCUBLAS_VERSION = '12.2.5.6-1'
#     NVIDIA_VISIBLE_DEVICES = 'all'
#     COLAB_JUPYTER_TRANSPORT = 'ipc'
#     NV_NVML_DEV_VERSION = '12.2.140-1'
#     NV_CUDNN_PACKAGE_NAME = 'libcudnn8'
#     CGROUP_MEMORY_EVENTS = '/sys/fs/cgroup/memory.events /var/colab/cgroup/jupyter-children/memory.events'
#     NV_LIBNCCL_DEV_PACKAGE = 'libnccl-dev=2.19.3-1+cuda12.2'
#     NV_LIBNCCL_DEV_PACKAGE_VERSION = '2.19.3-1'
#     VM_GCE_METADATA_HOST = '169.254.169.253'
#     HOSTNAME = 'f5eeb48a58d4'
#     LANGUAGE = 'en_US'
#     TBE_RUNTIME_ADDR = '172.28.0.1:8011'
#     COLAB_TPU_1VM = ''
#     GCE_METADATA_TIMEOUT = '3'
#     NVIDIA_REQUIRE_CUDA = ('cuda>=12.2 brand=tesla,driver>=470,driver<471 '
 'brand=unknown,driver>=470,driver<471 brand=nvidia,driver>=470,driver<471 '
 'brand=nvidiartx,driver>=470,driver<471 brand=geforce,driver>=470,driver<471 '
 'brand=geforcertx,driver>=470,driver<471 brand=quadro,driver>=470,driver<471 '
 'brand=quadrortx,driver>=470,driver<471 brand=titan,driver>=470,driver<471 '
 'brand=titanrtx,driver>=470,driver<471 brand=tesla,driver>=525,driver<526 '
 'brand=unknown,driver>=525,driver<526 brand=nvidia,driver>=525,driver<526 '
 'brand=nvidiartx,driver>=525,driver<526 brand=geforce,driver>=525,driver<526 '
 'brand=geforcertx,driver>=525,driver<526 brand=quadro,driver>=525,driver<526 '
 'brand=quadrortx,driver>=525,driver<526 brand=titan,driver>=525,driver<526 '
 'brand=titanrtx,driver>=525,driver<526')
#     NV_LIBCUBLAS_DEV_PACKAGE = 'libcublas-dev-12-2=12.2.5.6-1'
#     NV_NVTX_VERSION = '12.2.140-1'
#     COLAB_JUPYTER_IP = '172.28.0.12'
#     NV_CUDA_CUDART_DEV_VERSION = '12.2.140-1'
#     NV_LIBCUSPARSE_VERSION = '12.1.2.141-1'
#     COLAB_LANGUAGE_SERVER_PROXY_ROOT_URL = 'http://172.28.0.1:8013/'
#     NV_LIBNPP_VERSION = '12.2.1.4-1'
#     NCCL_VERSION = '2.19.3-1'
#     KMP_LISTEN_PORT = '6000'
#     TF_FORCE_GPU_ALLOW_GROWTH = 'true'
#     ENV = '/root/.bashrc'
#     PWD = '/content'
#     COLAB_LANGUAGE_SERVER_PROXY_REQUEST_TIMEOUT = '30s'
#     TBE_EPHEM_CREDS_ADDR = '172.28.0.1:8009'
#     TBE_CREDS_ADDR = '172.28.0.1:8008'
#     NV_CUDNN_PACKAGE = 'libcudnn8=8.9.6.50-1+cuda12.2'
#     NVIDIA_DRIVER_CAPABILITIES = 'compute,utility'
#     COLAB_JUPYTER_TOKEN = ''
#     LAST_FORCED_REBUILD = '20240627'
#     NV_NVPROF_DEV_PACKAGE = 'cuda-nvprof-12-2=12.2.142-1'
#     NV_LIBNPP_PACKAGE = 'libnpp-12-2=12.2.1.4-1'
#     NV_LIBNCCL_DEV_PACKAGE_NAME = 'libnccl-dev'
#     TCLLIBPATH = '/usr/share/tcltk/tcllib1.20'
#     NV_LIBCUBLAS_DEV_VERSION = '12.2.5.6-1'
#     COLAB_KERNEL_MANAGER_PROXY_HOST = '172.28.0.12'
#     NVIDIA_PRODUCT_NAME = 'CUDA'
#     NV_LIBCUBLAS_DEV_PACKAGE_NAME = 'libcublas-dev-12-2'
#     USE_AUTH_EPHEM = '1'
#     NV_CUDA_CUDART_VERSION = '12.2.140-1'
#     COLAB_WARMUP_DEFAULTS = '1'
#     HOME = '/root'
#     LANG = 'en_US.UTF-8'
#     COLUMNS = '100'
#     CUDA_VERSION = '12.2.2'
#     CLOUDSDK_CONFIG = '/content/.config'
#     NV_LIBCUBLAS_PACKAGE = 'libcublas-12-2=12.2.5.6-1'
#     NV_CUDA_NSIGHT_COMPUTE_DEV_PACKAGE = 'cuda-nsight-compute-12-2=12.2.2-1'
#     COLAB_RELEASE_TAG = 'release-colab_20240703-060140_RC00'
#     PYDEVD_USE_FRAME_EVAL = 'NO'
#     KMP_TARGET_PORT = '9000'
#     CLICOLOR = '1'
#     KMP_EXTRA_ARGS = ('--logtostderr --listen_host=172.28.0.12 --target_host=172.28.0.12 '
 '--tunnel_background_save_url=https://colab.research.google.com/tun/m/cc48301118ce562b961b3c22d803539adc1e0c19/m-s-259gjb9haf0wy '
 '--tunnel_background_save_delay=10s '
 '--tunnel_periodic_background_save_frequency=30m0s '
 '--enable_output_coalescing=true --output_coalescing_required=true')
#     NV_LIBNPP_DEV_PACKAGE = 'libnpp-dev-12-2=12.2.1.4-1'
#     COLAB_LANGUAGE_SERVER_PROXY_LSP_DIRS = '/datalab/web/pyright/typeshed-fallback/stdlib,/usr/local/lib/python3.10/dist-packages'
#     NV_LIBCUBLAS_PACKAGE_NAME = 'libcublas-12-2'
#     COLAB_KERNEL_MANAGER_PROXY_PORT = '6000'
#     CLOUDSDK_PYTHON = 'python3'
#     NV_LIBNPP_DEV_VERSION = '12.2.1.4-1'
#     ENABLE_DIRECTORYPREFETCHER = '1'
#     NO_GCE_CHECK = 'False'
#     JPY_PARENT_PID = '86'
#     PYTHONPATH = '/env/python'
#     TERM = 'xterm-color'
#     NV_LIBCUSPARSE_DEV_VERSION = '12.1.2.141-1'
#     GIT_PAGER = 'cat'
#     LIBRARY_PATH = '/usr/local/cuda/lib64/stubs'
#     NV_CUDNN_VERSION = '8.9.6.50'
#     SHLVL = '0'
#     PAGER = 'cat'
#     COLAB_LANGUAGE_SERVER_PROXY = '/usr/colab/bin/language_service'
#     NV_CUDA_LIB_VERSION = '12.2.2-1'
#     NVARCH = 'x86_64'
#     NV_CUDNN_PACKAGE_DEV = 'libcudnn8-dev=8.9.6.50-1+cuda12.2'
#     NV_CUDA_COMPAT_PACKAGE = 'cuda-compat-12-2'
#     MPLBACKEND = 'module://ipykernel.pylab.backend_inline'
#     NV_LIBNCCL_PACKAGE = 'libnccl2=2.19.3-1+cuda12.2'
#     LD_LIBRARY_PATH = '/usr/local/nvidia/lib:/usr/local/nvidia/lib64'
#     COLAB_GPU = ''
#     GCS_READ_CACHE_BLOCK_SIZE_MB = '16'
#     NV_CUDA_NSIGHT_COMPUTE_VERSION = '12.2.2-1'
#     NV_NVPROF_VERSION = '12.2.142-1'
#     LC_ALL = 'en_US.UTF-8'
#     COLAB_FILE_HANDLER_ADDR = 'localhost:3453'
#     PATH = '/root/.buildozer/android/platform/apache-ant-1.9.4/bin:/opt/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/tools/node/bin:/tools/google-cloud-sdk/bin'
#     NV_LIBNCCL_PACKAGE_NAME = 'libnccl2'
#     COLAB_DEBUG_ADAPTER_MUX_PATH = '/usr/local/bin/dap_multiplexer'
#     NV_LIBNCCL_PACKAGE_VERSION = '2.19.3-1'
#     PYTHONWARNINGS = 'ignore:::pip._internal.cli.base_command'
#     DEBIAN_FRONTEND = 'noninteractive'
#     COLAB_BACKEND_VERSION = 'next'
#     COLAB_CUSTOMIZE_FOR_VM_TYPE = '1'
#     OLDPWD = '/'
#     _ = '/usr/local/bin/buildozer'
#     PACKAGES_PATH = '/root/.buildozer/android/packages'
#     ANDROIDSDK = '/root/.buildozer/android/platform/android-sdk'
#     ANDROIDNDK = '/root/.buildozer/android/platform/android-ndk-r25b'
#     ANDROIDAPI = '33'
#     ANDROIDMINAPI = '21'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2
