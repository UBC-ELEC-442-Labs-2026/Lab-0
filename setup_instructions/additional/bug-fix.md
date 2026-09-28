# QArm Keyboard Navigator Temporary Bug Fix

**Last updated:** September 24, 2026  

> This is a temporary workaround for a bug in the Quanser QArm Python library. If Quanser fixes the issue in a future update, this change may no longer be required.

## Problem

When running the QArm Keyboard Navigator, you may see an error similar to:

```text
ValueError: not enough values to unpack (expected 3, got 2)
```

The issue is in Quanser's `qarm.py` file. The QArm Keyboard Navigator currently expects `forward_kinematics()` to return three values, but the function returns only two.

## Fix

If you followed the recommended installation location in `personal-software-installation.md`, your Quanser Academic Resources repository should be located at:

```text
C:\Users\<your-user-name>\Documents\Quanser
```

If you installed it somewhere else, use your own Quanser repository location instead.

1. Open **VS Code**.

2. Open a VS Code terminal with:

   ```text
   Ctrl + `
   ```

3. Navigate to the folder containing `qarm.py`:

   ```text
   cd ~/Documents/Quanser/0_libraries/python/hal/products
   ```

4. Open `qarm.py` in VS Code:

   ```text
   code qarm.py
   ```

5. Go to **line 343** and find:

   ```python
   ee_position, ee_rotation, gamma = self.armMath.forward_kinematics(phi=initialPose)
   ```

6. Replace that line with:

   ```python
   ee_position, ee_rotation = self.armMath.forward_kinematics(phi=initialPose)
   gamma = 0
   ```

7. Save the file