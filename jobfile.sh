#!/bin/bash -l
#
#SBATCH --ntasks=16
#SBATCH --time=06:00:00
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=1000
#SBATCH --export=NONE

unset SLURM_EXPORT_ENV

singularity run --bind /home/vault/b116ba/b116ba17/workshop/output:/user/source/output --bind /home/vault/b116ba/b116ba17/workshop/stable-diffusion-v1-5:/user/source/stable-diffusion-v1-5 workshop-d2s-image.sif --prompt "Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k , toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon, jungle , green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture painting"
