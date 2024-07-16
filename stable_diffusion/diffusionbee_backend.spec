# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['diffusionbee_backend.py'],
    pathex=['../model_converter', '../stable_diffusion_tf_models'],
    binaries=[],
    datas=[('../model_converter', 'model_converter'),
        ('../stable_diffusion_tf_models', 'stable_diffusion_tf_models'),
        ('../stable_diffusion', 'stable_diffusion'),
        ('stable_diffusion/clip_tokenizer/bpe_simple_vocab_16e6.txt.gz', '.'),
    ('stable_diffusion/clip_tokenizer/xl_text_projection_mat.npy', '.')],
    hiddenimports=['tensorflow','tensorflow_metal', 'tensorflow_addons'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='diffusionbee_backend',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          upx_exclude=[],
          argv_emulation=False,
          runtime_tmpdir=None,
          target_arch='x86_64',
          codesign_identity='Developer ID Application: Chien Ming Wang (7JXF7HB32R)',
          )

app = BUNDLE(
    exe,
    name='diffusionbee_backend.app',
    icon=None,
    bundle_identifier='com.deeparch.diffusionbee_backend'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='diffusionbee_backend',
)
