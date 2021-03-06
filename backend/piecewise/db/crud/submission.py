from sqlalchemy.orm import Session

from piecewise.db.models.submission import Submission
from piecewise.db.schemas.submission import SubmissionCreate


def get_submissions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Submission).offset(skip).limit(limit).all()


def create_submission(db: Session, submission: SubmissionCreate):
    print("CREATE_SUBMISSION")
    db_item = Submission(**submission.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
