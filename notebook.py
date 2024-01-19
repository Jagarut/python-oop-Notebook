import datetime

# store the next available id for all new notes
last_id = 0

class Note:
    """
    Represent a note in the notebook. Match against string in searches 
    and stores tags for each note.
    """
    def __init__(self, memo, tags="") -> None:
        """
        Initialize a note with a memo and optional space-separated tags.
        Automatically set the note's creation date and unique id
        """
        global last_id
        last_id += 1
        self.id = last_id
        self.memo = memo
        self.tags = tags
        self.creatation_date = datetime.datetime.today()

    def match(self, query):
        """
        Determines if this note maches the filter text. Return True
        if it matches False otherwise.

        Search is case sensitive and matches both text and tags.
        """
        return query in self.memo or query in self.tags
    
class Notebook:
    """
    Represent a collection of notes that can be tagged, modified, and searched.
    """

    def __init__(self) -> None:
        """
        Initialize a notebook with and empty list
        """
        self.notes = []

    def new_note(self, memo, tags=""):
        """
        Creates new note and adds it the notebook
        """
        new_note = Note(memo, tags)
        self.notes.append(new_note)

    def _find_note(self, note_id):
        try:
            note = self.notes[int(note_id) - 1]
            return note
        except:
            return None

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and changes its
        memo to the given value.
        """
        note = self._find_note(note_id)
        note.memo = memo

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and changes its
        tags to the given value.
        """
        note = self._find_note(note_id)
        note.tags = tags

    def search(self, query):
        """
        Find all notes that maches the given query string
        """
        found_notes = []

        for note in self.notes:
            if note.match(query):
                found_notes.append(note)

        return found_notes