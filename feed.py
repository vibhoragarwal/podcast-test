import yaml
import xml.etree.ElementTree as xml_tree


with open('feed.yaml') as f:
    data = yaml.safe_load(f)

    link_prefix = data['link']

    rss_element = xml_tree.Element('rss', {    'version' : '2.0',
    'xmlns:itunes' : 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content' : 'http://purl.org/rss/1.0/modules/content/'})
    channel_element = xml_tree.SubElement(rss_element, 'channel')
    xml_tree.SubElement(channel_element, 'title').text = data['title']
    xml_tree.SubElement(channel_element, 'subtitle').text = data['subtitle']
    xml_tree.SubElement(channel_element, 'itunes:author').text = data['author']
    xml_tree.SubElement(channel_element, 'description').text = data['description']
    xml_tree.SubElement(channel_element, 'format').text = data['format']
    xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix+data['image']})
    xml_tree.SubElement(channel_element, 'language').text = data['language']
    xml_tree.SubElement(channel_element, 'link').text = link_prefix
    xml_tree.SubElement(channel_element, 'itunes:category', {'text': data['category']})

    for item in data['item']:
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = item['title']
        xml_tree.SubElement(item_element, 'itunes:author').text =  data['author']
        xml_tree.SubElement(item_element, 'itunes:description').text = item['description']
        xml_tree.SubElement(item_element, 'pubDate').text = item['published']
        xml_tree.SubElement(item_element, 'title').text = item['title']
        enclosure = xml_tree.SubElement(item_element, 'enclosure', {'url': link_prefix+item['file'], 'type': 'audio/mpeg', 'length': item['length']})

    output_tree = xml_tree.ElementTree(rss_element)
    output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)