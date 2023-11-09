from django.shortcuts import render, redirect, get_object_or_404
from base.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

def new_conversation(self, request, id):

    item = get_object_or_404(Item, self, id=id)

    if item.created_by == request.user:
        redirect('dashboard/')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add('request.user')
            conversation.members.add('created_by')
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('detail', id=id)
    else:
        form = ConversationMessageForm()

    context = {
        'form': form,
        'conversations': conversation,
        'title': new_conversation
    }
    
    return render(request, 'conversation/conversation.html', context)