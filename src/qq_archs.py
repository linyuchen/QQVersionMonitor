from enum import StrEnum

class QQArchExt(StrEnum):
    DMG = '.dmg'
    AMD64_EXE = 'x64.exe'
    X86_EXE = 'x86.exe'
    ARM64_EXE = 'arm64.exe'
    AMD64_DEB = 'amd64.deb'
    ARM64_DEB = 'arm64.deb'
    X64_RPM = 'x86_64.rpm'
    ARM64_RPM = 'aarch64.rpm'
    X64_APPIMAGE = 'x86_64.AppImage'
    ARM64_APPIMAGE = 'arm64.AppImage'
    LOONGARCH64_DEB = 'loongarch64.deb'
    MIPS64EL_DEB = 'mips64el.deb'


QQ_EXT_DESC_MAP = {
    QQArchExt.DMG: 'macOS',
    QQArchExt.AMD64_EXE: 'Windows 64位',
    QQArchExt.X86_EXE: 'Windows 32位',
    QQArchExt.AMD64_DEB: 'Debian Linux x64',
    QQArchExt.ARM64_DEB: 'Debian Linux ARM64',
    QQArchExt.X64_RPM: 'RPM Linux x64',
    QQArchExt.ARM64_RPM: 'RPM Linux ARM64',
    QQArchExt.X64_APPIMAGE: 'Linux x64',
    QQArchExt.ARM64_APPIMAGE: 'Linux ARM64',
    QQArchExt.LOONGARCH64_DEB: 'Debian Linux 龙芯',
    QQArchExt.MIPS64EL_DEB: 'Debian Linux MIPS64',
}