from dataclasses import dataclass

from .qq_archs import QQArchExt, QQ_EXT_DESC_MAP


@dataclass
class QQDownloadLink:
    arch_ext: QQArchExt
    description: str
    link: str = ''

    def __hash__(self):
        return self.link.__hash__()


class QQDownloadLinkManager:
    def __init__(self):
        self.links: set[QQDownloadLink] = set()

    def get_link_by_ext(self, ext: QQArchExt) -> QQDownloadLink | None:
        for link in self.links:
            if link.arch_ext == ext:
                return link
        return None

    def add_link(self, url: str):
        for arch_ext in QQArchExt.__members__.values():
            if url.endswith(arch_ext.value):
                description = QQ_EXT_DESC_MAP.get(arch_ext)
                link = QQDownloadLink(arch_ext=arch_ext, description=description, link=url)
                self.links.add(link)
                return link
        raise Exception(f'{url} unknown ext')