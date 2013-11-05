from django import template
import re

register = template.Library()

@register.filter
def tags_to_css(tags):
	#import ipdb; ipdb.set_trace()
	new_tags = []
	for i in range(len(tags)):
		new_tags.append(re.sub("\s", "_", str(tags[i])))
	new_tags = " ".join(new_tags)
	return new_tags.lower()

@register.filter
def tag_to_css(tag):
	new_tag = re.sub("\s", "_", str(tag))
	return new_tag.lower()

